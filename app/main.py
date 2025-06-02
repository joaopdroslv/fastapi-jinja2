from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates

from app.modules import user

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")


@app.get("/")
async def healthy():
    return JSONResponse(status_code=200, content={"success": True})


# This route uses Jinja2 to render HTML on the server (Server-Side Rendering - SSR).
# It embeds the user data directly into the HTML before sending it to the client,
# eliminating the need to return JSON and use JavaScript on the client side to render content.
@app.get("/users", response_class=HTMLResponse)
async def users(request: Request):
    users = user.get_all_users()

    return templates.TemplateResponse(
        "users.html", {"request": request, "users": users}
    )
