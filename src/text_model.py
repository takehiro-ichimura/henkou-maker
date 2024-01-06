from enum import Enum

class ParseMode(Enum):
    USE_PARAGRAPH = 1
    USE_BR = 2

class TextModel:
    textlines = []

    def __init__(self, textlines):
        self.textlines = textlines
    
    # ファイルをimportし、クラスを初期化する
    @classmethod
    def create(cls, fileName):
        file = open(fileName, 'r')
        textlines = file.readlines()
        return cls(textlines)

    def __parseUseParagpaph(self):
        out = ""

        for x in self.textlines:
            if x == "\n":
                out += "<br>"
            else:
                out += ("<p>"+x.replace("\n","")+"</p>")
            out += "\n"

        return out
    
    def __parseUseBr(self):
        out = "<p>"

        for x in self.textlines:
            if x == "\n":
                out += "<br>"
            else:
                out += (x.replace("\n","<br>"))
            out += "\n"
        
        out += "</p>"
        return out
    
    def __parse(self, parseMode):
        if (parseMode == ParseMode.USE_PARAGRAPH):
            return self.__parseUseParagpaph()
        else:
            return self.__parseUseBr()


    def export(self, parseMode = ParseMode.USE_BR):
        output = self.__parse(parseMode)
        print(output)
    