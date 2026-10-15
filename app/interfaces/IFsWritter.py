import abc

class IFsWritter(abc.ABC):
    @abc.abstractmethod
    def write_folder(self, directory) -> str:
        pass

    @abc.abstractmethod
    def write_file_with_path(self, full_path) -> str:
        pass