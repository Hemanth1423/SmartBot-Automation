from pathlib import Path
from typing import Any, Dict, Optional

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn
from fastapi.staticfiles import StaticFiles
from fellowup_mails.success_mail import send_email
from database_operations.db_process import insert_contact

app = FastAPI()

templates_dir = Path(__file__).resolve().parent / "templates"
templates = Jinja2Templates(directory=str(templates_dir))
app.mount("/static", StaticFiles(directory="static"), name="static")


def render_template(
    request: Request,
    template_name: str,
    context: Optional[Dict[str, Any]] = None,
):
    template_context = {"request": request, **(context or {})}
    try:
        return templates.TemplateResponse(
            request=request,
            name=template_name,
            context=template_context,
        )
    except TypeError as exc:
        if "request" not in str(exc):
            raise
        return templates.TemplateResponse(template_name, template_context)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return render_template(request, "index.html")


@app.post("/contact")
async def contact(
    name: str = Form(...),
    email: str = Form(...),
    company: str = Form(...),
    message: str = Form(...)
):

    insert_contact(name, email, company, message)
    send_email(name, email, company, message)

    return {
        "status": "success"
    }




if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)