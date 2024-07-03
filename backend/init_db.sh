#!/bin/sh
echo "Initializing database..."
python3 -c 'from app import db, app; with app.app_context(): db.create_all()'
echo "Database initialized."



