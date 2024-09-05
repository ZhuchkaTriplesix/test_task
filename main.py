import uvicorn
import config
from fastapi import Depends, HTTPException
from starlette.responses import HTMLResponse
from configuration.app import App
from fastapi.openapi.docs import get_swagger_ui_html

app = App().app


@app.get("/api/docs", response_class=HTMLResponse)
async def get_docs() -> HTMLResponse:
    return get_swagger_ui_html(openapi_url="/api/openapi.json", title="docs")


if __name__ == "__main__":
    uvicorn.run(app, **config.uvicorn.dict())
