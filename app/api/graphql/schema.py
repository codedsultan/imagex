import strawberry
from strawberry.fastapi import GraphQLRouter
from app.api.graphql.queries import Query
from app.api.graphql.mutations import Mutation

schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)
