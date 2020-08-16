# Author: Anton Mikhaylov
# Created: 16/08/2020

from json import JSONDecodeError
from typing import Dict, Any

from aiohttp import web

from app.api.http.exception import HTTPRequestException
from app.dto import LogRecordOptionsDTO
from app.manager.log import LogRecordManager

__all__ = [
    'LogRecordHandler',
]


class LogRecordHandler:
    """
    Logger request handler
    """

    def __init__(self, log_manager: LogRecordManager) -> None:
        self.__log_manager = log_manager

    async def get_list(self, request: web.Request) -> web.Response:
        """
        Getting request with options and return log record list.
        :param request:
        :return:
        """

        try:
            options = await self.__parse_request(request)

        except HTTPRequestException as http_err:
            return web.json_response(
                status=200,
                data={
                    "ok": False,
                    "error": str(http_err)
                }
            )

        try:
            record_list = self.__log_manager.get_list(options)

        except Exception as err:
            return web.json_response(
                status=200,
                data={
                    "ok": False,
                    "error": str(err)
                }
            )

        return web.json_response(
            status=200,
            data={
                "ok": True,
                **record_list.dict(),
            }
        )

    async def __parse_request(self, request: web.Request) -> LogRecordOptionsDTO:
        """
        Validate request body
        :param request:
        :return:
        """

        try:
            request = await request.json()

            offset = int(request["offset"])
            limit = int(request.get("limit") or 10)

            if limit < 0 or offset < 0:
                raise HTTPRequestException(
                f"""Offset or limit contain invalid value. All value in this fields must be above zero.
                Current request {request}"""
            )

            options = LogRecordOptionsDTO(
                offset=offset,
                limit=limit,
            )

        except JSONDecodeError as decode_err:
            raise HTTPRequestException(
                f"Request body must be JSON."
            )

        except KeyError as key_err:
            raise HTTPRequestException(
                f"Requirement field doesnt found in request.\nCurrent request: {request}"
            )

        except ValueError as val_err:
            raise HTTPRequestException(
                f"One or more field in request contain invalid value.\nCurrent request: {request}"
            )

        else:
            return options
