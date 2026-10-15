import abc

class ILog(abc.ABC):
    @abc.abstractmethod
    def message(string_message: str) -> None:
        pass
