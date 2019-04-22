# 用于操作数据库的类
class UserModel(object):
    # 定义初始用户
    users = {
        1: {"name": "余承建", "age": 22, "tall": 175},
        2: {"name": "欧阳甘霖", "age": 17, "tall": 170},
        3: {"name": "林永奇", "age": 24, "tall": 180},
        4: {"name": "邓少强", "age": 28, "tall": 165}
    }

    # 获取单个用户 使用类方法 不能自动触发
    @classmethod
    def get(cls, user_id):
        '''
        cls：表示当前类UserModel
        :param user_id:需要获取到的用户id
        :return: 返回用户id对应的数据信息
        '''
        return cls.users[user_id]

    # 修改用户数据
    @classmethod
    def update(cls, user_id, age, tall):
        '''

        :param user_id: 用户id
        :param age:  表示传过来的新的age信息，就是修改后的age
        :param tall: 表示传过来的新的tall信息，就是修改后的tall
        :return: 无
        '''
        cls.users[user_id]["age"] = age
        cls.users[user_id]["tall"] = tall

        return cls.users[user_id]

    # 删除单个用户
    @classmethod
    def delete(cls, user_id):
        '''
        执行删除
        :param user_id:删除指定id数据
        :return:
        '''
        return cls.users.pop(user_id)

    #获取所有用户
    @classmethod
    def get_all(cls):
        return cls.users
    #创建新用户
    @classmethod
    def creat(cls,*args):
        '''

        :param args: 接收的是用户信息元组
        :return:
        '''
        new_user_id=max(cls.users.keys())+1
        #创建新用户返回
        cls.users[new_user_id]={"name":args[0],"age":args[1],"tall":args[2]}
        return cls.users

