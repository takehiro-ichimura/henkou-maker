from enum import Enum

class ParseMode(Enum):
    USE_PARAGRAPH = 1
    USE_BR = 2

# TODO: 複雑になってきたら、jinja2などの利用を検討する
class TextModel:
    template = ''

    issue = ''
    title = ''
    author = ''
    content = []

    output = ''

    def __init__(self, issue, title, author, content, template):
        self.issue = issue
        self.title = title
        self.author = author
        self.content = content

        self.template = template
        self.output = template
    
    # ファイルをimportし、クラスを初期化する(in.txt形式)
    @classmethod
    def create(cls, fileName, templateFilename):
        inputFile = open(fileName, 'r')
        inputLines = inputFile.readlines()

        issue = inputLines[0]
        title = inputLines[1]
        author = inputLines[2]
        content = inputLines[3:]

        templateFile = open(templateFilename, 'r')
        template = templateFile.read()
        return cls(issue, title, author, content, template)
        
    def __update(self, tagName, content):
        self.output = self.output.replace(r"{{"+ tagName + r"}}", content)

    def __createContentUseParagpaph(self):
        out = ""
        for x in self.content:
            if x == "\n":
                out += "<br>"
            else:
                out += ("<p>"+x.replace("\n","")+"</p>")
            out += "\n"
        return out
    
    def __createContentUseBr(self):
        out = "<p>"
        for x in self.content:
            if x == "\n":
                out += "<br>"
            else:
                out += (x.replace("\n","<br>"))
            out += "\n"
        out += "</p>"
        return out
    
    def __createContent(self, parseMode):
        contentTagName = 'content'
        if (parseMode == ParseMode.USE_PARAGRAPH):
            self.__update(contentTagName, self.__createContentUseParagpaph())
        else:
            self.__update(contentTagName, self.__createContentUseBr())
    
    def __createIssue(self):
        issueTagName = 'issue'
        self.__update(issueTagName, self.issue)
    
    def __createTitle(self):
        titleTagName = 'title'
        self.__update(titleTagName, self.title)
    
    def __createAuthor(self):
        authorTagName = 'author'
        self.__update(authorTagName, self.author)
    
    # テンプレートを更新し、ファイルを出力する
    def export(self, parseMode = ParseMode.USE_BR):
        self.__createIssue()
        self.__createTitle()
        self.__createAuthor()
        self.__createContent(parseMode)
        print(self.output)
    