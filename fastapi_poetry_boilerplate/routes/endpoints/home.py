"""
Fastapi Poetry Boilerplate.

A boilerplate for fastapi python project supported by poetry.
"""

from fastapi import APIRouter

import fastapi_poetry_boilerplate.schemas.general as general_schema
from fastapi_poetry_boilerplate.core.config_parser import config

router = APIRouter()

APP_NAME = config['meta']['app_name']


@router.get('/',
            summary="Home Page",
            response_model=general_schema.Message,
            responses={
                404: {"model": general_schema.Message},
                500: {"model": general_schema.Message}})
async def home():
    """
    Fastapi Poetry Boilerplate.

    A boilerplate for fastapi python project supported by poetry.
    """
    return {
        'msg': f'{APP_NAME} APIs is working. '
        'Use /docs or /redoc to see the documentation.'}
