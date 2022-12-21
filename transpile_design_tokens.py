import json
import os
import datetime

DESIGN_TOKENS_PATH = os.path.join(os.getcwd(), "design_tokens/design-tokens.tokens.json")


class TranspilerFigmaToken:
    """Class to transpile colors
    """
    def __init__(self):
        self._tokens_qtd = 0
        self._json_obj = self._load_json_design()

    def __repr__(self):
        """class representation
        :return:
        """
        return f"<FigmaTranspiler {self._tokens_qtd} tokens>"

    @staticmethod
    def _load_json_design() -> dict:
        """Read json file
        :return:
        """
        return json.load(open(DESIGN_TOKENS_PATH))

    def _save_on_file(self):
        """Read and write color on file in src/utils/colors.py
        :return:
        """
        if not os.path.exists(os.path.join(os.getcwd(), "src/utils")):
            os.mkdir(os.path.join(os.getcwd(), "src/utils"))

        with open(f"{os.path.join(os.getcwd(), 'src/utils/colors.py')}", 'w') as file:
            file.write(f"""# ===========================================================
# Generated by TranspilerFigmaToken on {datetime.datetime.now()} 
# 
# This class generate {len(self._json_obj["color"].keys())} colors
# 
# Github of Author: https://github.com/Pedro-Augusto-Barbosa-Aparecido
# ===========================================================\n
            """)

            colors = self._json_obj["color"].keys()

            file.write("""
class Color:""")

            for color in colors:
                file.write(f"""
    # {color.capitalize()} section\n""")
                if list(self._json_obj["color"][color].keys())[0].isdigit():
                    _colors = self._json_obj["color"][color].keys()

                    for _color_intensity in _colors:
                        file.write(f"    {color.upper()}_{_color_intensity} = \"{self._json_obj['color'][color][_color_intensity]['value'].upper()}\"\n")
                else:
                    file.write(f"    {color.upper()} = \"{self._json_obj['color'][color]['value'].upper()}\"\n")

    def transpile(self):
        """call transpile function
        :return:
        """
        self._save_on_file()


if __name__ == "__main__":
    transpiler = TranspilerFigmaToken()
    transpiler.transpile()