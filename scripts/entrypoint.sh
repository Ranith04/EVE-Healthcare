#!/bin/bash
set -e

# Run migrations (We will enable this once alembic is configured in Step 2)
# alembic upgrade head || true

exec uvicorn app.main:app --host 0.0.0.0 --port 8000
