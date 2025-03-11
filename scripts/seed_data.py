# fastapi-backend/scripts/seed_data.py
import asyncio
from app.db.session_postgres import async_session
from app.db.models.sql.template import Template

async def seed():
    async with async_session() as session:
        # Example seed data for templates
        sample_templates = [
            {"name": "Template A", "product_type": "tshirt", "view_angle": "front", "model_type": "unisex", "template_path": "templates/template_a.png"},
            {"name": "Template B", "product_type": "tshirt", "view_angle": "back", "model_type": "unisex", "template_path": "templates/template_b.png"}
        ]
        for tmpl in sample_templates:
            new_template = Template(**tmpl)
            session.add(new_template)
        await session.commit()
        print("Seeding complete.")

if __name__ == "__main__":
    asyncio.run(seed())
