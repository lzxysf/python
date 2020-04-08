'''
python中使用SAX或DOM解析XML
SAX是事件驱动模型，通过在解析XML过程中触发一个个的事件，并调用用户定义的回调函数来处理XML文件
DOM是将XML在内存中解析成一个树，通过数的操作来操作XML

SAX适合对大型文件进行处理，只需要文件的部分内容即可
一个 DOM 的解析器在解析一个 XML 文档时，一次性读取整个文档，把文档中所有元素保存在内存中的一个树结构里，之后你可以利用DOM 提供的不同的函数来读取或修改文档的内容和结构，也可以把修改过的内容写入xml文件

SAX不在叙述
DMO实例如下
'''

from xml.dom.minidom import parse
import xml.dom.minidom


dom_tree = parse('../others/movies.xml')
collections = dom_tree.documentElement
if collections.hasAttribute('shelf'):
    shelf = collections.getAttribute('shelf')
    shelf_str = str(shelf)
    print(shelf_str.center(60, '*'))

movies = collections.getElementsByTagName('movie')
movie.getElementsByTagName('type')

for movie in movies:
    if movie.hasAttribute('title'):
        title = movie.getAttribute('title')
        print(title.center(40, '\''))
        type = movie.getElementsByTagName('type')[0].childNodes[0].data
        print('type:' + type)
        format = movie.getElementsByTagName('format')[0].childNodes[0].data
        print('format:' + format)

