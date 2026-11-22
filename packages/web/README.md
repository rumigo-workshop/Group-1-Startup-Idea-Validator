# Startup Idea Validator Web

React, TypeScript, and Vite frontend for the project.

## Local development

```powershell
npm install
npm run dev
```

The app is normally available at `http://localhost:5173`.

## Production checks

```powershell
npm run lint
npm run build
```

## Docker

Build the production image from this directory:

```powershell
docker build --build-arg VITE_API_URL=http://localhost:8000 -t startup-idea-validator-web .
```

Run it on port 5173:

```powershell
docker run --rm -p 5173:80 startup-idea-validator-web
```

Open `http://localhost:5173`. The image builds the Vite bundle in a Node image, then serves the static output with Nginx. Client-side routes fall back to `index.html`.

## API configuration

The frontend defaults to `http://localhost:8000`. To target another API while building the image, pass the Vite variable as a build argument through your chosen Docker build setup, or create a local `.env.local` for non-container development:

```env
VITE_API_URL=http://localhost:8000
```

Never commit `.env.local` or credentials.
