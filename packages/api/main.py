from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app =FastAPI(
    title="Author Management API",
    description="API for managing authors and their information",
    version="1.0.0"
)

authors=[]

class Author(BaseModel):
    name: str
    nationality: str


class Work(BaseModel):
    title: str

@app.post("/authors")
def add_author(author: Author):

    new_author = {
        "id": len(authors) + 1,
        "name": author.name,
        "nationality": author.nationality,
        "works": []
    }

    authors.append(new_author)

    return {
        "message": "Author added successfully",
        "author": new_author
    }

@app.get("/authors")
def get_authors():
    return {
        "message": "Authors fetched successfully",
        "authors": authors
    }

@app.get("/authors/{author_id}")
def get_author(author_id: int):

    for author in authors:
        if author["id"] == author_id:
            return {
                "message": "Author found successfully",
                "author": author
            }

    raise HTTPException(
        status_code=404,
        detail="Author not found"
    )
@app.delete("/authors/{author_id}")
def delete_author(author_id: int):

    for author in authors:
        if author["id"] == author_id:
            authors.remove(author)

            return {
                "message": "Author deleted successfully",
                "author": author
            }

    raise HTTPException(
        status_code=404,
        detail="Author not found"
    )

@app.post("/authors/{author_id}/works")
def add_work(author_id: int, work: Work):

    for author in authors:
        if author["id"] == author_id:

            author["works"].append(work.title)

            return {
                "message": "Work added successfully",
                "author": author
            }

    raise HTTPException(
        status_code=404,
        detail="Author not found"
    )
    
@app.get("/authors/{author_id}/works")
def get_author_works(author_id: int):

    for author in authors:
        if author["id"] == author_id:

            return {
                "message": "Author's works fetched successfully",
                "author_name": author["name"],
                "works": author["works"]
            }

    raise HTTPException(
        status_code=404,
        detail="Author not found"
    )