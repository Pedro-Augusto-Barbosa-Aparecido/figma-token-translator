from abc import ABC, abstractclassmethod
from typing import Any


class ArgValidator(ABC):
  @abstractclassmethod
  def __init__(self) -> None:
    pass

  @staticmethod
  def has_argument(parser, argument_name: str):
    arguments = parser._get_kwargs()

    for argument in arguments:
      if argument_name in argument:
        return True
    return False
