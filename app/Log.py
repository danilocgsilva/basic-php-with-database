from app.interfaces.ILog import ILog

class Log(ILog):
    @staticmethod
    def message(string_message: str) -> None:
        print(string_message)
