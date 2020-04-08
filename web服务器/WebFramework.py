import time

html_root_dir = './html/'


class Application(object):
    def __init__(self, urls):
        self.urls = urls

    def __call__(self, env, start_response):
        path = env.get("PATH_INFO", "/")
        if path.startswith("/static"):
            file_name = path[8:]
            file_path = html_root_dir + file_name
            try:
                file = open(file_path, "rb")
            except Exception:
                status = '404 Not Found'
                headers = []
                start_response(status, headers)
                return "file not found"
            else:
                data = file.read()
                file.close()
                status = '200 OK'
                headers = []
                start_response(status, headers)
                return data.decode('utf-8')

        for url,handler in urls:
            if url == path:
                return handler(env, start_response)

        status = '404 Not Found'
        headers = []
        start_response(status, headers)
        return 'not found'

def show_time(env, start_response):
    status = '200 OK'
    headers = []
    start_response(status, headers)
    return '当前时间:' + str(time.ctime())

def say_hello(env, start_response):
    status = '200 OK'
    headers = []
    start_response(status, headers)
    return 'hello'

urls = [
    ('/', show_time),
    ('/saytime', show_time),
    ('/sayhello', say_hello)
]

app = Application(urls)
