import tornado.web
import tornado.ioloop
# print(tornado.version)

'''
tornado接口实质：
接收一个http的请求（长的url），分析长链接当中
的数据，判断是以什么样的方式进行请求的（get,post,delete,put,etc），
然后返回指定的数据（代码主要做的事情,需要对数据库进行操作）
'''

#定义处理http请求得处理类
class MainHandler(tornado.web.RequestHandler):

    #定义处理get请求的类,如果使用get请求，则自动调用
    def get(self, *args, **kwargs):

        #write是指定返回的数据 这里是字符串
        #不仅可以返回字符串 页可以返回html(被渲染之后的)
        self.write("<h1>hello world tornado</h1>")

    def put(self, *args, **kwargs):
        pass

    def post(self, *args, **kwargs):
        pass

    def delete(self, *args, **kwargs):
        pass


if __name__ == '__main__':

    #创建App对象
    #第一个参数是请求的url，第二个参数是处理url的处理类
    app=tornado.web.Application([
        ("/tornado",MainHandler)
    ])
    #监听一个本地的端口
    app.listen(8888)
    print("正在监听端口8888：。。。")
    #启动tornado服务,一直处于监听状态
    tornado.ioloop.IOLoop.current().start()


'''
常见错误：
1文件命名，
2请求方式get，pos发生错误
3端口被占用
'''




