import sys

import argparse
import logging


class CLI: 
  CURRENT_VERSION_CLI = "Figma Token Translator (FTT) - 0.0.1"
  CURRENT_VERSION_FILE_TRANSLATOR = "File Translator (FT) - 0.0.0"

  DEVELOPER = "Developed by Pedro Augusto - <https://github.com/Pedro-Augusto-Barbosa-Aparecido>"

  def __init__(self) -> None:
    logging.info(f"CLI {self.CURRENT_VERSION_CLI} - Figma Token Translator")

    self.parser = argparse.ArgumentParser(
      prog="Figma Token Translator",
      description=f"Translator for tokens generateds by extention of Figma {self.CURRENT_VERSION_CLI}",
      epilog=self.DEVELOPER,
      usage="%(prog)s [options]"
    )

    self.parser.version = self.CURRENT_VERSION_CLI
    self.parser.add_argument("-v", "--version", action="version")

    subparser = self.parser.add_subparsers(help="File Translator", dest="command")
    self._create_sub_parser(subparser)

    parser_args = self.parser.parse_args()
    
    if parser_args:
      pass
    else:
      self.parser.print_help()
      sys.exit(0)

  def _create_sub_parser(self, subparser): 
    self.translator_by_file = subparser.add_parser(
      "file", 
      help="Translate Figma json file",
      description="File Translator module",
      epilog=self.DEVELOPER
    )

    self.translator_by_file.version = self.CURRENT_VERSION_FILE_TRANSLATOR

    self.translator_by_file.add_argument("-v", "--version", action="version")
    self.translator_by_file.add_argument("-fp", "--filepath", type=str, default=".", help="JSON File path [default is Current Dir]", required=False)
    self.translator_by_file.add_argument("-f", "--file", type=str, help="filename", required=True)
    self.translator_by_file.add_argument("-o", "--out", type=str, help="(Optional) Type of translator output, supports [class, namedtuple, dict, constants] | default = 'class'", default="class", required=False)
