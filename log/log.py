import os

from rich.console import Console


class Logger:
  def __init__(self) -> None:
    self._console = Console()
    self._file = os.path.abspath(".")
