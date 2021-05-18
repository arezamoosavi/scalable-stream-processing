#!/bin/sh


set -o errexit
set -o nounset

echo ". . . . . Web Boot Up Is Done! . . . . ."

uvicorn run_api:app --host ${HOST} --port ${FASTAPI_PORT} --reload --ws 'auto' --loop 'auto' --workers 4

exec "$@"
