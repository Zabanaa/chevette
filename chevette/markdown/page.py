from .parser import MarkdownDocument


class Page(MarkdownDocument):

    def __init__(self, path):
        self.path = path
        self.is_page = True
