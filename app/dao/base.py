# Author: Anton Mikhaylov
# Created: 16/08/2020
from abc import ABC, abstractmethod
from typing import Dict, Any, List


class BaseDAO(ABC):

    __instance: 'BaseDAO' = None

    def __new__(cls) -> 'BaseDAO':
        """Constructor with singleton
        :return: ChannelDAO object
        """

        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
            cls._records = []

        return cls.__instance

    @abstractmethod
    def get_list(self, options: Dict[str, Any]) -> List[Dict[str,Any]]:
        raise NotImplemented()
