import strawberry
from typing import List

@strawberry.type
class Query:
    @strawberry.field
    async def templates(self) -> List[str]:
        # In a real implementation, you’d fetch this data from a repository.
        return ["Template A", "Template B"]
