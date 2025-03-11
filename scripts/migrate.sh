#!/bin/bash
echo "Starting database migration..."
if [ "$DB_TYPE" = "postgres" ]; then
    echo "Running PostgreSQL migrations using Alembic..."
    alembic upgrade head
elif [ "$DB_TYPE" = "mongodb" ]; then
    echo "MongoDB does not require migrations. Skipping."
else
    echo "Unsupported DB_TYPE: $DB_TYPE"
fi
echo "Migration completed."
