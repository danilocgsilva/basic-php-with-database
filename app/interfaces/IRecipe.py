import abc
from app.File import File

class IRecipe(abc.ABC):
    @abc.abstractmethod
    def get_files(self) -> list[File]:
        pass
