#!/bin/bash
echo "Starting database backup..."
if [ "$DB_TYPE" = "postgres" ]; then
    echo "Backing up PostgreSQL database..."
    pg_dump -h localhost -U $POSTGRES_USER $POSTGRES_DB > backup.sql
elif [ "$DB_TYPE" = "mongodb" ]; then
    echo "Backing up MongoDB database..."
    mongodump --uri="$MONGODB_URL" --out backup/
else
    echo "Unsupported DB_TYPE: $DB_TYPE"
fi
echo "Backup completed."
