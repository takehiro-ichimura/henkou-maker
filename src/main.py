from text_model import ParseMode, TextModel

INPUT_FILE = './in.txt'
TEMPLATE_FILENAME = './templates/template.html'

def main():
    textModel = TextModel.create(INPUT_FILE, TEMPLATE_FILENAME)
    textModel.export(parseMode=ParseMode.USE_BR)

if __name__ == "__main__":
    main()