# Author: Anton Mikhaylov
# Created: 16/08/2020

from app.config import CONFIGURATION

from app.dao import LogRecordDAO
from app.dao.exception import DAOException
from app.dto import LogRecordOptionsDTO, LogRecordListDTO
from app.manager.exception import LogRecordManagerException

__all__ = [
    'LogRecordManager',
]


class LogRecordManager:
    """
    Log record Manager
    """

    def __init__(self):

        self.__log_record_dao = LogRecordDAO()

    def get_list(self, options: LogRecordOptionsDTO) -> LogRecordListDTO:
        """
        Getting element list from storage by options
        :param options:
        :return:
        """

        try:
            return self.__log_record_dao.get_list(options)

        except DAOException as d_err:
            raise LogRecordManagerException(d_err)
