from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.modules import user

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    users = user.get_all_users()

    return templates.TemplateResponse(
        "homepage.html", {"request": request, "users": users}
    )
