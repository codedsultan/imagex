# FastAPI Image Processing Service

This project is a modular, loosely coupled FastAPI backend that supports:
- Multiple database backends (PostgreSQL or MongoDB)
- Multiple storage backends (Local or S3/MinIO)
- Pluggable image processing services (Pillow and OpenCV)
- REST and GraphQL APIs

## Setup

1. Copy `.env.example` to `.env` and adjust configuration as needed.
2. Install requirements:
   ```bash
   pip install -r requirements/dev.txt
   ```
3. Run migrations and seed data:
   ```bash
   alembic upgrade head
   ```
4. Run the server:
   ```bash
   uvicorn app.main:app --reload
   ```

## Usage

### REST API

The REST API is mounted at `/rest` and supports the following endpoints:

- `/rest/process-image`: Processes an image using the configured mockup service.

### GraphQL API

The GraphQL API is mounted at `/graphql` and supports the following queries:

- `/graphql/templates`: Returns a list of templates.

## Testing

To run tests, use the following command:

```bash
pytest
```

## Deployment

To deploy the application, you can use Docker Compose. Create a `docker-compose.override.yml` file and adjust the configuration as needed. Then, run:

```bash
docker-compose up -d
```

## License

This project is licensed under the MIT License.


## Acknowledgements

Developed by [Olusegun Ibraheem](https://github.com/codedsultan).
