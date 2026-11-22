
import sqlite3
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Book Management API")

# Allow communication with React + Vite
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database file stored alongside main.py
DB_PATH = Path(__file__).resolve().parent / "books.db"


# Connect to SQLite database
def get_connection():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


# Create database table automatically
def init_db():
    connection = get_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            price REAL NOT NULL
        )
    """)

    connection.commit()
    connection.close()


init_db()


# Book model
class Book(BaseModel):
    title: str
    author: str
    price: float


# Home route
@app.get("/")
def home():
    return {"message": "Book API is running"}


# GET - Get all books
@app.get("/books")
def get_books():
    connection = get_connection()

    rows = connection.execute(
        "SELECT * FROM books ORDER BY id"
    ).fetchall()

    connection.close()

    return [dict(row) for row in rows]


# GET - Get a single book
@app.get("/books/{book_id}")
def get_book(book_id: int):
    connection = get_connection()

    row = connection.execute(
        "SELECT * FROM books WHERE id = ?",
        (book_id,)
    ).fetchone()

    connection.close()

    if row is None:
        raise HTTPException(status_code=404, detail="Book not found")

    return dict(row)


# POST - Add a book
@app.post("/books", status_code=201)
def post_book(book: Book):
    connection = get_connection()

    cursor = connection.execute(
        "INSERT INTO books (title, author, price) VALUES (?, ?, ?)",
        (book.title, book.author, book.price)
    )

    connection.commit()

    new_book_id = cursor.lastrowid

    row = connection.execute(
        "SELECT * FROM books WHERE id = ?",
        (new_book_id,)
    ).fetchone()

    connection.close()

    return dict(row)


# DELETE - Delete a book
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    connection = get_connection()

    row = connection.execute(
        "SELECT * FROM books WHERE id = ?",
        (book_id,)
    ).fetchone()

    if row is None:
        connection.close()
        raise HTTPException(status_code=404, detail="Book not found")

    connection.execute(
        "DELETE FROM books WHERE id = ?",
        (book_id,)
    )

    connection.commit()
    connection.close()

    return {
        "message": "Book deleted successfully",
        "deleted_book": dict(row)
    }
