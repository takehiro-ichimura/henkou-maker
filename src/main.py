import os
import sys
from text_model import ParseMode, TextModel

def main():
    print('##### STARTED')
    exe_path = os.path.dirname(os.path.abspath(sys.argv[0]))
    textModel = TextModel.create(exe_path + '/../input/input.txt', exe_path + '/../templates/template.html')
    textModel.export(parseMode=ParseMode.USE_BR, output_path=exe_path + '/../output/')

if __name__ == "__main__":
    main()