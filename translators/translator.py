import os
import json
import logging


class Translator:
  def __init__(self, json_file_path: str = None) -> None:
    logging.info("Verifing file path!!")
    if json_file_path is None:
      logging.fatal("JSON File path is missing!")
      raise ValueError("JSON File path is missing!")

    if not os.path.exists(json_file_path) or not os.path.isfile(json_file_path):
      logging.fatal("File not exists or path is director or is incorrect path!")
      raise IOError("File not exists or path is director or is incorrect path!")
    
    if not json_file_path.endswith(".json"):
      logging.fatal("File passed isn't a .json")
      raise Exception("File passed isn't a .json")

    logging.info("File is accepted!!")
    self._json_path = json_file_path
    self._qtd_tokens = {}

  @property
  def temp_path(self): 
    return os.path.join(
      os.getcwd(),
      "temp"
    )

  @property
  def path(self):
    return self._json_path

  @property 
  def json(self):
    json_content = None
    
    try: 
      with open(self._json_path, "rb") as json_file:
        json_content = json.load(json_file)
      logging.info("JSON file is load!!")
      logging.info(f"Content: {json_content}")
      return json_content
    except Exception as e:
      logging.error(f"Error on load json file error: {e.args}")

  def add_token_qtd(self, token: str, token_qtd: int):
    logging.info(f"Registring token {token}!!")
    if token in self._qtd_tokens.keys():
      logging.warning("Token quantity is replaced!!")

    self._qtd_tokens[token] = token_qtd
    