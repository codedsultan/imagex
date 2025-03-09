from typing import List, Optional
from app.db.repositories.base_repository import BaseRepository
from app.core.config import settings

if settings.DB_TYPE.lower() == "postgres":
    from sqlalchemy.ext.asyncio import AsyncSession
    from sqlalchemy.future import select
    from app.db.models.sql.template import Template as SQLTemplate

    class TemplateRepositorySQL(BaseRepository[SQLTemplate]):
        def __init__(self, session: AsyncSession):
            self.session = session
        
        async def get(self, id: int) -> Optional[SQLTemplate]:
            result = await self.session.execute(select(SQLTemplate).where(SQLTemplate.id == id))
            return result.scalars().first()
        
        async def list(self) -> List[SQLTemplate]:
            result = await self.session.execute(select(SQLTemplate))
            return result.scalars().all()
        
        async def create(self, obj_in: dict) -> SQLTemplate:
            new_template = SQLTemplate(**obj_in)
            self.session.add(new_template)
            await self.session.commit()
            await self.session.refresh(new_template)
            return new_template
        
        async def update(self, id: int, obj_in: dict) -> SQLTemplate:
            template = await self.get(id)
            for key, value in obj_in.items():
                setattr(template, key, value)
            self.session.add(template)
            await self.session.commit()
            await self.session.refresh(template)
            return template
        
        async def delete(self, id: int) -> None:
            template = await self.get(id)
            if template:
                await self.session.delete(template)
                await self.session.commit()

elif settings.DB_TYPE.lower() == "mongodb":
    from app.db.models.mongo.template import Template as MongoTemplate
    from motor.motor_asyncio import AsyncIOMotorDatabase

    class TemplateRepositoryMongo(BaseRepository[MongoTemplate]):
        def __init__(self, db: AsyncIOMotorDatabase):
            self.collection = db.templates
        
        async def get(self, id: str) -> Optional[MongoTemplate]:
            data = await self.collection.find_one({"_id": id})
            if data:
                return MongoTemplate(**data)
            return None
        
        async def list(self) -> List[MongoTemplate]:
            cursor = self.collection.find()
            result = []
            async for document in cursor:
                result.append(MongoTemplate(**document))
            return result
        
        async def create(self, obj_in: dict) -> MongoTemplate:
            result = await self.collection.insert_one(obj_in)
            obj_in["_id"] = result.inserted_id
            return MongoTemplate(**obj_in)
        
        async def update(self, id: str, obj_in: dict) -> MongoTemplate:
            await self.collection.update_one({"_id": id}, {"$set": obj_in})
            data = await self.collection.find_one({"_id": id})
            return MongoTemplate(**data)
        
        async def delete(self, id: str) -> None:
            await self.collection.delete_one({"_id": id})
