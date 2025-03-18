from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.exceptions import RequestValidationError
import logging
import random
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from utils.url import URLRelation
from db.memory.db import MemoryDB

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

db = MemoryDB()

class URLBody(BaseModel):
    url: str

@app.exception_handler(RequestValidationError)
async def error_handler(request, exc):
    message = f'ERROR: {request} - {exc}'
    logging.error(message)
    return JSONResponse(content={"message": message})

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(
        name="index.html", request=request
    )

@app.post("/url", response_class=JSONResponse)
async def gen_short_url(request: Request, body: URLBody):
    url_relation = URLRelation(url=body.url, host=request.client.host)
    db.save(url_relation)
    return JSONResponse(content={
        "short_url": url_relation.short_url
    })

@app.get("/c/{code}")
async def hit_short(request: Request, code: str):
    redirect_url = db.find(code)
    if not redirect_url:
        return templates.TemplateResponse(
            name="not_found.html", request=request
        )
    return RedirectResponse(redirect_url)
