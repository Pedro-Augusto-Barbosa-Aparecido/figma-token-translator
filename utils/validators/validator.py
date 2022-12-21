import os

from abc import ABC, abstractclassmethod


class PathValidator(ABC):
  @abstractclassmethod
  def __init__(self) -> None:
    pass

  @staticmethod
  def validate_path(path: str):
    return not os.path.exists(path)
