import argparse
import logging
import sys

from translators.class_translator import ClassTranslator
from translators.constants_translators import ConstantsTranslator
from translators.dict_translator import DictTranslator
from translators.namedtuple_translator import NamedtupleTranslator
from utils.validators.arg_validator import ArgValidator


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
      logging.info(f"Loading json file from {parser_args.filepath}")
      filepath = parser_args.filepath if parser_args.filepath != '.' else None

      match parser_args.out:
        case "class": 
          if not ArgValidator.has_argument(parser_args, "filename"):
            logging.warning("Filenames translated will be assumed name each token")

            translator = ClassTranslator(filepath)
          else:
            logging.warning(f"Filenames translated will be assumed {parser_args.filename}-" + "{token_name}.py")
            translator = ClassTranslator(filepath, parser_args.filename)
        case "namedtuple":
          if not ArgValidator.has_argument(parser_args, "filename"):
            logging.warning("Filenames translated will be assumed name each token")

            translator = NamedtupleTranslator(filepath)
          else:
            logging.warning(f"Filenames translated will be assumed {parser_args.filename}-" + "{token_name}.py")
            translator = NamedtupleTranslator(filepath, parser_args.filename)
        case "dict":
          if not ArgValidator.has_argument(parser_args, "filename"):
            logging.warning("Filenames translated will be assumed name each token")

            translator = DictTranslator(filepath)
          else:
            logging.warning(f"Filenames translated will be assumed {parser_args.filename}-" + "{token_name}.py")
            translator = DictTranslator(filepath, parser_args.filename)
        case "constants":
          if not ArgValidator.has_argument(parser_args, "filename"):
            logging.warning("Filenames translated will be assumed name each token")

            translator = ConstantsTranslator(filepath)
          else:
            logging.warning(f"Filenames translated will be assumed {parser_args.filename}-" + "{token_name}.py")
            translator = ConstantsTranslator(filepath, parser_args.filename)
        case _:
          logging.warning("Invalid type output!")
          sys.exit(0)

      logging.info(f"Output file type will be {parser_args.out}")
      translator.translate(output_path=parser_args.destination)
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
    self.translator_by_file.add_argument("-fp", "--filepath", type=str, help="JSON File path [default is Current Dir]", required=True)
    self.translator_by_file.add_argument("-d", "--destination", type=str, default=".", help="Output path for translated files", required=False)
    self.translator_by_file.add_argument("-f", "--filename", type=str, help="(Optional) Filename of each token generated ex: 'YOUR_NAME-TOKEN_NAME.py' . Default is token name", required=False)
    self.translator_by_file.add_argument("-o", "--out", type=str, help="(Optional) Type of translator output, supports [class, namedtuple, dict, constants] | default = 'class'", default="class", required=False)
