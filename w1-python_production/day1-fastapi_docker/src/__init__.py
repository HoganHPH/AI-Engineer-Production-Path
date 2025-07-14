from fastapi import FastAPI

from .config import Settings
from .services.networks.connection import connect_networks


settings = Settings()

def create_app() -> FastAPI:
    app = FastAPI(
        title="FastAPI app",
        description="This is FastAPI app.",
    )

    return app

# Create the FastAPI application instance
app = create_app()

# Include the API router
from .routers import page_home, ml_page

app = connect_networks(app)
app.include_router(page_home.router)
app.include_router(ml_page.ml_router)
