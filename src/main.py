from text_model import ParseMode, TextModel

INPUT_FILE = './in.txt'

def main():
    textModel = TextModel.create(INPUT_FILE)
    textModel.export(parseMode=ParseMode.USE_BR)

if __name__ == "__main__":
    main()