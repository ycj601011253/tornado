import sys
#表示把当前位置移动到上一层
sys.path.append("..")
from models.users import UserModel
import tornado.web#创建web应用
#将json数据序列化为可以返回给前端的字符串数据
from tornado.escape import json_encode

#定义处理单个用户的类,继承处理请求的类
class UserHandlers(tornado.web.RequestHandler):
    #获取单个用户数据

    def get(self,user_id):

        '''
        :param user_id:是一个字符串，需要转换为int格式
        :return:如果没有查找到指定的数据，则返回404
        '''
        try:
            #查询指定的id返回的数据
            user=UserModel.get(int(user_id))
        except KeyError:
            #返回哟长数据 异常信息不要写中文
            resp={"status":False,"msg":"select failure"}
            info=json_encode(resp)
            info="""
            <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <title>Title</title>
                </head>
                <body>
                {}
                </body>
            </html>
            """.format(info)
            self.write(info)
            return self.set_status(404)
        #返回正常数据
        self.write(json_encode(user))
    #修改单个用户数据
    def put(self,user_id):
        '''

        :param user_id:接收url传过来的参数
        :return: 返回的提示信息
        '''
        #接收body传过来的age和tall参数
        age=self.get_argument("age")
        tall=self.get_argument("tall")
        result=UserModel.update(int(user_id),age,tall)
        #执行修改的过程
        if result:
            resp={"status":True,"msg":"update success","data":result}
            self.write(json_encode(resp))
    #删除指定用户id数据
    def delete(self,user_id):
        #执行删除，并返回删除的数据
        result=UserModel.delete(int(user_id))
        #定义提示信息
        if result:
            resp={"status":True,"msg":"delete success","data":result}
            self.write(json_encode(resp))

#定义操作所有用户的类
class UserListHandlers(tornado.web.RequestHandler):

    #获取所有有用户信息
    def get(self):
        #调用get_all函数 获取所有的用户信息
        data=UserModel.get_all()
        #返回提示信息
        resp={"status":True,"msg":"get all success","data":data}
        #返回编码后的数据
        self.write(json_encode(resp))

    #创建新用户
    def post(self, *args, **kwargs):

        #接收body传过来的参数
        name=self.get_argument("name")
        age=self.get_argument("age")
        tall=self.get_argument("tall")

        data=UserModel.creat(name,age,tall)
        resp={"status":True,"msg":"create success","data":data}
        self.write(json_encode(resp))



