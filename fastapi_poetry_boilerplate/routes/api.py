"""
Fastapi Poetry Boilerplate.

A boilerplate for fastapi python project supported by poetry.
"""

from fastapi import APIRouter

from fastapi_poetry_boilerplate.routes.endpoints import home

router = APIRouter()

router.include_router(home.router, tags=["Home"])
