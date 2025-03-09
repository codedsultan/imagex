from typing import Generic, TypeVar, List, Optional

ModelType = TypeVar("ModelType")

class BaseRepository(Generic[ModelType]):
    async def get(self, id: str) -> Optional[ModelType]:
        raise NotImplementedError
    
    async def list(self) -> List[ModelType]:
        raise NotImplementedError
    
    async def create(self, obj_in: dict) -> ModelType:
        raise NotImplementedError
    
    async def update(self, id: str, obj_in: dict) -> ModelType:
        raise NotImplementedError
    
    async def delete(self, id: str) -> None:
        raise NotImplementedError
