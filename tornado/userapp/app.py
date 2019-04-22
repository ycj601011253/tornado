import tornado.ioloop
import tornado.web
import tornado.httpserver
from handles.users import *

#第一个参数是路由，
# 第二个是路由处理类 会将user_id传给路由处理类
#UserHandlers 处理单个用户的类

HEADLERS=[
    (r"/api/user/(\d+)",UserHandlers),
    (r"/api/users",UserListHandlers),
]

def run():
    #创建app的web应用
    app=tornado.web.Application(
        HEADLERS,
        debug=True,#修改文件之后不用重启tornado服务
    )
    #使用非阻塞单线程的服务器
    http_server=tornado.httpserver.HTTPServer(app)
    #监听指定端口
    http_server.listen(8888)
    print("正在监听：8888......")
    #启动服务
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    run()


