from http.server import HTTPServer, SimpleHTTPRequestHandler


class ChevetteRequestHandler(SimpleHTTPRequestHandler):

    def do_GET(self):
        SimpleHTTPRequestHandler.do_GET(self)

    # TODO: implement do_404
    # def do_404(self):
    #     pass


class ChevetteServer(HTTPServer):
    pass
