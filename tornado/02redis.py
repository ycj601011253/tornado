import redis

class RedisText:

    def __init__(self):
        self.r=self.conn_redis()
        # self.str_text()
        # self.hash_text()
        # self.list_text()
        # self.set_text()
        self.zset_text()
    #连接数据库
    def conn_redis(self):
        return redis.Redis(host="127.0.0.1",port=6379)

    #字符串
    def str_text(self):
        self.r.set("name","oygl")
        self.get("name")
        self.r.get("name")
        self.r.strlen("name")

    #获取字符串类型数据对应的值，是一个byte类型
    def get(self,name):
        result=self.r.get(name)

    def hash_text(self):
        self.r.hset("student","name","weiliang")
        result=self.r.hget("student","name")
        print(result)
        self.r.hget("student","name")
        self.r.hdel("student","name")
        self.r.hexists("student","name")
        self.r.hgetall("student")
        self.r.hset("student","age",19)
        self.r.hincrby("student","age",20)
        self.r.hkeys("student")
        self.r.hvals("students")
        self.r.hlen("student")
        self.r.hmget("student","name","age")
        self.r.hsetnx("student","name","zs")


    def list_text(self):
        self.r.lpush("list1","age","shengao")
        result=self.r.lrange("list1",0,-1)
        print(result)
        self.r.lrange("list1",0,-1)
        self.r.ltrim("list1",1,0)
        self.r.llen("list1")
        self.r.lpop("list1")
        self.r.rpop("list1")
        self.r.lindex("list1",10)
        self.r.lrem("list1",2,"hello")

    def set_text(self):
        self.r.sadd("myset5",3,"helbt")
        result=self.r.smembers("myset5")
        print(result)
        self.r.scard("myset5")
        self.r.sdiff("myset5","myset4")
        self.r.sdiffstore("diff","myset5","myset4")
        self.r.smove("myset5","myset4","hello")
        self.r.smembers("myset5")
        self.r.sismember("myset5","zhangsan")
        self.r.sinter("myset5","myset4")
        self.r.sunion("myset5","myset4")

    def zset_text(self):
        self.r.zadd("zset5",{"age":5})
        result=self.r.zrange("zset5",0,-1,withscores=True)
        print(result)
        self.r.zrange("zset5",0,-1,withscores=True)
        self.r.zcard("zset5")
        self.r.zrem("zset5","zhsng")
        self.r.zcount("zset5",0,-1)
        self.r.zrank("zset5","zhang")
        self.r.zrevrank("zset5","zhang")
        self.r.zremrangebyrank("zset5",1,10)
        self.r.zremrangebyscore("zset5",0,100)


if __name__ == '__main__':
    RedisText()



