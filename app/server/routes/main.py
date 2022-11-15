from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

router = APIRouter()

templates = Jinja2Templates(directory="app/server/templates")


@router.get("/", include_in_schema=False)
async def get_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@router.get("/login", include_in_schema=False)
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@router.get("/app", include_in_schema=False)
async def app(request: Request):
    return templates.TemplateResponse("app.html", {"request": request})


@router.get("/api-docs", include_in_schema=False)
async def docs(request: Request):
    return RedirectResponse(url="/docs")
