import tornado.ioloop
import tornado.web
import os


port = 8888
db_path = "./data.db"
pages = {
    "main_page": "./html/Main.html",
    "skills_page": "./html/Skills.html",
}


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(pages["main_page"])

class SkillsHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(pages["skills_page"])

def make_app():
   return tornado.web.Application([
        (r"/", MainHandler),
        (r"/skills", SkillsHandler),
        (r"/static/(.*)", tornado.web.StaticFileHandler, 
{"path": "./static"})
    ], debug=True)

if __name__ == "__main__":
    app = make_app()  
    app.listen(port)  
    tornado.ioloop.IOLoop.current().start()  

