# str() 函数返回一个用户易读的表达形式
# repr() 函数返回一个解释器易读的表达形式
s = 'hello, world'
print(str(s))
print(repr(s))

hello = 'hello,runbin\n'
hellos = repr(hello)
print(hellos)

print('*'*20)

# rjust, ljust, center, zfill
str1 = '123'
print(str1.rjust(5))  # 右对齐，共5个字符，不够用空格补全，够了原样输出
print(str1.ljust(5))  # 左对齐，共5个字符，不够用空格补全，够了原样输出
print(str1.center(5)) # 中间对齐，共5个字符，不够用空格补全，够了原样输出
print(str1.zfill(5))  # 右对齐，共5个字符，不够用0补全，够了原样输出

print('*'*20)

# format
print('my name is {},my age is {}'.format('lsf', 21))
print('{0},{1}'.format('google', 'baidu'))
print('{1},{0}'.format('google', 'baidu'))
print('{0},{1},{a}'.format('google', 'baidu', a='taobao'))

print('%s,%s,%s' % ('google', 'baidu', 'taobao'))

print('*'*20)

# 读取键盘输入
str = input('请输入')
print('你输入的内容是'+str)
