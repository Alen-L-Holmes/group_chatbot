# from pydantic import BaseSettings
from pydantic import BaseModel, Extra


class Config(BaseModel, extra=Extra.ignore):
    group_id: list = [123456789]
    hour: int = 9
    minute: int = 30

    pass


if __name__ == '__main__':
    pass
