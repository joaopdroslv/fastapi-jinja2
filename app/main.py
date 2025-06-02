from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates

from app.modules import user

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")


@app.get("/")
async def healthy():
    return JSONResponse(status_code=200, content={"success": True})


@app.get("/users", response_class=HTMLResponse)
async def users(request: Request):
    users = user.get_all_users()

    return templates.TemplateResponse(
        "users.html", {"request": request, "users": users}
    )
