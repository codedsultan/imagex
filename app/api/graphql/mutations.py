import strawberry

@strawberry.type
class Mutation:
    @strawberry.mutation
    async def dummy_mutation(self) -> str:
        return "Mutation executed successfully"
