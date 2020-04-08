import re

# re.match
# 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功则返回none
# re.match(pattern, string, flags)
# pattern匹配的正则表达式,string要匹配的字符串,flags标志位,用于匹配正则表达式的匹配方式，如是否匹配大小写，是否多行等
'''
flags是一个正则表达式修饰符-可选标志
多个标志可以通过|来指定
re.I  使匹配对大小写不敏感
re.L  使本地化识别匹配
re.M  多行匹配
re.S  使.匹配包括换行符在内的所有字符

'''

print(re.match('abc', 'abc123'))  # 返回一个描述，如 <_sre.SRE_Match object; span=(0, 3), match='abc'> 
print(re.match('abc', 'abc123').group())  # 匹配开头,group方法返回分组字符串，如果没有匹配到会报错的

print('*'.center(30, '*'))
print(re.match('abc', 'labc123'))  # re.match从字符串起始位置开始，不是起始位置匹配不到的

# re.search
# re.search(pattern, string, flags)
# 用于查找字符串中可以匹配成功的子串，从字符串的开始位置匹配到结尾，匹配成功即返回一个匹配结果且不再向后匹配，匹配失败返回None
print('*'.center(30, '*'))
result = re.search(r'\d', '3df78ii90who')
print(result)
print(result.group())

# re.split
# re.split(pattern, string, maxsplit=0, flags=0)
# maxsplit指定最大的分割次数，不指定为全部分割
# re.split以列表的形式返回匹配的对象
print('re.split'.center(30, '*'))
result = re.split('[0-9]', 'a1b2c3')
print(result)
# re.split根据匹配去切割字符串，并返回一个列表，注意，此处返回的是一个列表
print('split'.center(30, '*'))
result = re.split(r':|,', 'name:xiaoli,xiaowang,fangfang')
print(result)

# re.findall
# re.findall(pattern, string, flags = 0)
# 搜索string,以列表的形式返回全部能匹配到的字符串
print('re.findall'.center(30, '*'))
result = re.findall(r'\d', '3df78ii90who')
print(result)

# re.sub
# re.sub(pattern, repl, string, count=0,flags=0)
# 使用repl替换string中每一个字符串，返回替换后的字符串
# count用于指定最多替换的次数，不知道时全部替换
print('re.sub'.center(30, '*'))
# 例子：将字符串中连续的两个数字替换为00
result = re.sub('[0-9]{2}', '00', '2d345efii78')
print(result)

# sub进阶
# sub中的repl可以是一个函数，也可以是正则表达式
print('re.sub进阶'.center(30, '*'))


def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)


result = re.sub(r'(?P<value>\d+)', double, 'A23B45d8h81')
print(result)


s = "you're asking me out.that's so cute.what's your name again?"
print(re.sub(r"([.!?])", r"\1\n", s))

# group groups
print('group'.center(30, '*'))
result = re.match(r'(\w+) is (\w+)', 'he is a beijinger')
print(result)
print(result.group())   # 整体被匹配的字符串
print(result.group(1))  # pattern中第一个括号中的内容
print(result.group(2))  # pattern中第二个括号中的内容
print(result.groups())  # pattern中所有组的内容，以元组的形式返回

# compile
# compile函数用于编译正则表达式，生成一个正则表达式对象，供match、search、findall等函数使用
# 使用compile可以指定搜索的起始位置
print('compile'.center(30, '*'))
pattern = re.compile(r'\d+')
result = pattern.match('flo345wne')
print(result)

result = pattern.match('flo345wne', 3)
print(result.group())
print(result.start())  # 返回匹配开始的位置
print(result.end())    # 返回匹配结束的位置
print(result.span())   # 返回匹配位置，元组形式(开始位置，结束位置)


# 关闭贪婪模式演示，从网址中提取出来图片地址
print('贪婪模式'.center(30, '*'))

# re.split根据匹配去切割字符串，并返回一个列表，注意，此处返回的是一个列表
print('split'.center(30, '*'))
result = re.split(r':|,', 'name:xiaoli,xiaowang,fangfang')
print(result)

# 关闭贪婪模式演示，从网址中提取出来图片地址,使用了+？而非+
print('贪婪模式'.center(30, '*'))

s = """<img data-original="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" src="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" style="display: inline;">
"""
# 提取第一张图片地址
result = re.search(r'https.+?\.jpg', s)
print(result.group())

# 提取所有图片地址
result = re.findall(r'https.+?\.jpg', s)
print(result)
