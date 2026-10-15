class File:
    def __init__(self, path: str, content: str):
        self._path = path
        self._content = content

    @property
    def path(self) -> str:
        return self._path

    @property
    def content(self) -> str:
        return self._content
