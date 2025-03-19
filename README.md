# [URL Shortener](https://url-shortener-fastapi-dmzt.onrender.com)

## What is it?

A simple application where you paste any URL and get a short URL that can be used to redirect to your site.

## How can I use it?

1. You paste any URL in the input.
2. Click `SHORT IT!`
3. Click `COPY` to copy the URL to the clipboard
4. Share the URL

## What is it made of?

- Python
- [FastAPI](https://fastapi.tiangolo.com/)
- HTML
- CSS
- Javascript

## How it works?

I save the URLs in memory related to an alphanumeric code of size 6.

### Endpoints

- `GET /`
  Render the main page
- `POST /url`
  Generates the code, save the URL in memory and returns the short URL. The body JSON format is:

```json
{
  "url": "string"
}
```

- `GET /c/{code}`
  Searches for the code in memory. If exists it's redirected. If not render Not Found page.
