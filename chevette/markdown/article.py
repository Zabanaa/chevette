from .parser import MarkdownDocument


class Article(MarkdownDocument):

    def __init__(self, path):
        self.path = path
