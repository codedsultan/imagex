from app.dependencies import get_mockup_service
from app.services.mockup_service_interface import MockupServiceInterface

def get_api_mockup_service() -> MockupServiceInterface:
    """
    Dependency injection for REST API endpoints.
    This can simply call the global injector.
    """
    return get_mockup_service()
