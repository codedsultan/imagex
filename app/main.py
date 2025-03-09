from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.services.pillow_mockup_service import PillowMockupService  # or use global dependency
from app.api.rest.routes import router as rest_router
from app.api.graphql.schema import graphql_app

app = FastAPI(title="FastAPI Image Processing Service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/process-image")
async def process_image(payload: dict):
    # Here you can choose your service via dependency injection.
    from app.dependencies import get_mockup_service
    service = get_mockup_service()
    return service.process_mockup(payload)

# Include REST routes.
app.include_router(rest_router, prefix="/rest")

# Mount GraphQL endpoint.
app.mount("/graphql", graphql_app)
