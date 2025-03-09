from fastapi import APIRouter, Depends, HTTPException
from app.api.rest.models import ProcessImageRequest, ProcessImageResponse
from app.api.rest.dependencies import get_api_mockup_service

router = APIRouter()

@router.post("/process-image", response_model=ProcessImageResponse)
async def process_image(
    request: ProcessImageRequest,
    mockup_service=Depends(get_api_mockup_service)
):
    try:
        result = mockup_service.process_mockup(request.dict())
        return ProcessImageResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
