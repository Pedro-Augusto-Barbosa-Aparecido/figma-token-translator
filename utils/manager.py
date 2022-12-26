import logging
import os
import shutil
import sys
from abc import ABC, abstractclassmethod


class FileManager(ABC):
  @abstractclassmethod
  def __init__(self) -> None:
    pass

  @staticmethod
  def move_files(directory_origin: str, directory_destination: str):
    if not os.path.exists(directory_origin) or not os.path.isdir(directory_origin):
      logging.fatal("Directory origin not exists!!")
      raise IsADirectoryError("Directory origin not exists!!")

    if not os.path.exists(directory_destination) or not os.path.isdir(directory_destination):
      logging.warning("Directory destination not exists!! System create directory for you")
      os.makedirs(directory_destination)

    for file in os.listdir(directory_origin):
      try:
        logging.info(f"Moving {file} to {directory_destination}.")
        shutil.move(os.path.join(directory_origin, file), os.path.join(directory_destination, file))
        logging.info("File was move.")
      except Exception as e:
        logging.exception(f"Exception: {e}")
        sys.exit(-1)
