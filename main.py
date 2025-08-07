from alembic import command
from alembic.config import Config
from fastapi import FastAPI
import uvicorn
from starlette.responses import RedirectResponse

from routes.organizations import router

app = FastAPI(
    title="Secunda test REST API",
    description="",
    version="0.0.1",
)


app.include_router(router)


@app.get("/", include_in_schema=False)
async def docs_redirect():
    return RedirectResponse(url='/docs')


def start_app():
    alembic_config = Config("alembic.ini")
    command.upgrade(alembic_config, "head")

    uvicorn.run(app, host="0.0.0.0", port=8005)


if __name__ == "__main__":
    start_app()
