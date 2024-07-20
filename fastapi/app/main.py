from fastapi import APIRouter
from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.models import Info

from api.routes import item, slack
from uvicorn import run

app = FastAPI(openapi_url="/api/docs/openapi.json")

@app.get("/api/docs", include_in_schema=False)
async def get_documentation():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        oauth2_redirect_url="/api/docs/oauth2-redirect.html",
    )

app.include_router(item.router, tags=["item"])
app.include_router(slack.router, tags=["slack"])

if __name__ == "__main__":
    run(app, host='0.0.0.0', port=80)