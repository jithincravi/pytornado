import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print(self.get_arguments(name='name'))
        self.write("Hello, "+self.get_arguments(name='name')[0])


def make_app():
    return tornado.web.Application([
        (r"/sayhello", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()