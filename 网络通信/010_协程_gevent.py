'''
greenlet已经实现了协程，但是这个还的人工切换，是不是觉得太麻烦了，不要捉急，python还有一个比greenlet更强大的并且能够自动切换任务的模块gevent

其原理是当一个greenlet遇到IO(指的是input output 输入输出，比如网络、文件操作等)操作时，比如访问网络，就自动切换到其他的greenlet，等到IO操作完成，再在适当的时候切换回来继续执行。

由于IO操作非常耗时，经常使程序处于等待状态，有了gevent为我们自动切换协程，就保证总有greenlet在运行，而不是等待IO
'''

'''
由于gevent在切换IO操作（文件IO、网络IO）时是自动完成的，所以gevent需要通过修改Python自带的一些阻塞式系统调用的标准库，包括socket、ssl、threading和 select等模块，而变为协程，这一过程需要在启动时通过monkey patch（猴子补丁）完成。

monkey patching需要放到第一行导入，否则会报错，所以把 from gevent import monkey,monkey.patch_all()要放到文件最前面。


'''

# gevent并发下载器
from gevent import monkey
import gevent
import urllib.request

monkey.patch_all()

def myDownload(url):
    print('GET:',url)
    resp = urllib.request.urlopen(url)
    data = resp.read()
    print('%d bytes received form %s'%(len(data), url))

# 不适用gevent的情形,每一个网络请求都会阻塞
# myDownload('http://www.baidu.com')
# myDownload('http://www.sina.com')
# myDownload('http://www.taobao.com')

# joinall是抢占了主线的执行，整体是阻塞的，阻塞了主线，但3个网络请求不会互相阻塞
gevent.joinall([
    gevent.spawn(myDownload, 'http://www.baidu.com/'),
    gevent.spawn(myDownload, 'http://www.sina.com/'),
    gevent.spawn(myDownload, 'http://www.taobao.com/'),
])
