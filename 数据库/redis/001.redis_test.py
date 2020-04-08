# 安装redis连接模块
# sudo pip install redis
import redis

def main():
    try:
        r = redis.StrictRedis(host='localhost',port=6379)
        # 方式一：根据数据类型的不同，调用相应的方法，完成读写
        r.set('d','C++')
        print(r.get('d'))
        # 方式二：pipline
        # 缓冲多条命令，然后一次执行，减少服务器与客户端之间的TCP数据包，从而提高效率
        pipe = r.pipeline()
        pipe.set('e','java')
        pipe.set('f','python')
        pipe.execute()
        print(r.mget('e','f'))
    except Exception:
        print('error')

if __name__ == "__main__":
    main()
