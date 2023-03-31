#!/bin/bash

alembic revision --autogenerate -m "initial"

alembic upgrade head

uvicorn app.main:app --host 0.0.0.0 --port 9000 --reload