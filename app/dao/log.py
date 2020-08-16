# Author: Anton Mikhaylov
# Created: 16/08/2020

import json

from pydantic import ValidationError

from app.config import CONFIGURATION
from app.dao.base import BaseDAO
from app.dao.exception import DAOException
from app.dto import LogRecordOptionsDTO, LogRecordListDTO


class LogRecordDAO(BaseDAO):
    """
    This class contain methods for working with log records storage

    """
    def __init__(self):
        if not self._records:
            self.__prepare_data()

    def __prepare_data(self):
        """
        This method read log file and parse him
        :return:
        """

        try:
            with open(CONFIGURATION['FILE_NAME']) as raw_records:
                for record in raw_records:
                    self._records.append(json.loads(record))

        except FileNotFoundError as f_err:
            raise DAOException("File not found")

    def get_list(self, options: LogRecordOptionsDTO) -> LogRecordListDTO:
        """
        This method getting records by options from local storage
        :param options:
        :return:
        """

        try:
            if options.offset > len(self._records):
                messages = []

            elif (options.offset + options.limit) > len(self._records):
                options.limit = len(self._records) - options.offset
                messages = self._records[options.offset:(options.offset + options.limit)]

            else:
                messages = self._records[options.offset:(options.offset + options.limit)]

            return LogRecordListDTO(
                amount=len(self._records),
                next_offset=options.offset+options.limit
                    if (options.offset+options.limit) < len(self._records) else len(self._records),
                offset=options.offset,
                messages=messages
            )

        except IndexError as i_err:
            raise DAOException(f"Invalid offset or limit\n Current options: {options.dict()}")

        except ValidationError as v_err:
            raise DAOException(v_err)
