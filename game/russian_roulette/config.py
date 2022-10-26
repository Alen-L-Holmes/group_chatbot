from typing import Tuple
from pydantic import BaseModel, Extra
from pathlib import Path


class Config(BaseModel, extra=Extra.ignore):
    max_bet_gold: int = 10000
    sign_gold: Tuple[int, int] = (200, 1000)
    russian_path: Path = Path()
