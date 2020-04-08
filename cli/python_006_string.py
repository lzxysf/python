# coding=utf-8

str = "hello world"
_str = "394959"
print (str[2:])
print (str*2)
print(str+_str)
print('hello' in str)
print('w' not in str)

print('\n')
# 字符串前加r或者R,其中的转义字符不进行转义,当作普通字符
print(r'\n')
print(R'\n')

a = "%d+%d=%d" % (3, 6, 9)
print(a)


# python中使用三引号,允许字符串跨行,并且字符串中可以包含换行符、制表符和其他特殊字符
# 三引号的用法是一对单引号或双引号
# 使用三引号得到的字符串是所见即所得的
errHTML = '''
<HTML><HEAD><TITLE>
Friends CGI Demo</TITLE></HEAD>
<BODY><H3>ERROR</H3>
<B>%s</B><P>
<FORM><INPUT TYPE=button VALUE=Back
ONCLICK="window.history.back()"></FORM>
</BODY></HTML>
'''
print(errHTML)


x = "hello world"
y = "hello"

print(x.capitalize())         # 首字母大写
print(x.center(20))           # 居中,20是字符串总长度
print(x.count('l'))           # 某字符出现的次数

b = x.encode(encoding="utf-8", errors="strict")       # 将字符串转成utf-8编码的字节数组bytes
print(b.decode(encoding="utf-8", errors="strict"))    # 将字节数组bytes以utf-8的形式解码成字符串

print(x.endswith('ld'))
print(x.startswith('hel'))
print(x.find('l'))                                    # 从左侧开始查找
print(x.rfind('l'))                                   # 从右侧开始查找

m = '123abcDEF'
print(m.isalnum())             # 字符串至少有一个字符,且所有字符必须是字母或数字,为True,否则为False
print(m.isalpha())             # 字符串至少有一个字符,且所有字符必须是字母,......
print(m.isdigit())             # 字符串至少有一个字符,且所有字符必须是数字,......
print(m.islower())             # 所有区分大小写的字符都是小写的话,返回True,......
print(m.isupper())             # 所有区分大小写的字符都是大写的话,返回True,......

q = '*'
s = ['1', '2', 'three']
print(q.join(s))               # 以q为分隔符,将s中所有元素的字符串表示合并成一个新的字符串

print(len(m))

print(m.replace('123', '一二三'))  # 将字符串m中的字符串'123'替换为字符串'一二三'
print(m)                          # 替换后字符串m的值是不变的,说明replace中只是复制了m不是引用

m = '123 564 983 990'
n = ' '
print(m.split(' '))               # 以n为分隔符分割字符串m
print(errHTML.splitlines())       # 将errHTML的每一行作为一个元素进行分割