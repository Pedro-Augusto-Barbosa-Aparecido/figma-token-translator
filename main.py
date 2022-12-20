from logging import basicConfig, DEBUG, FileHandler, StreamHandler, Formatter
from cli import CLI

formatter = Formatter(
  "[%(asctime)s - %(levelname)s] (%(name)s): %(message)s",
  datefmt="%Y-%m-%d %H:%M:%S"
)

file_handler = FileHandler("log-cli.log", "w")
file_handler.formatter = formatter

stream_handler = StreamHandler()
stream_handler.setFormatter(formatter)

basicConfig(
  level=DEBUG,
  encoding="utf-8",
  handlers=[file_handler, stream_handler],
)

if __name__ == "__main__":
  cli = CLI()
