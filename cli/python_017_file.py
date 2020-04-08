print('write'.center(30, '*'))
f = open('../others/abc.txt', 'w')
num = f.write("python is a very good language\n")
num += f.write("java is a very good language too\n")
print('输入到文件中的字节长度为%d' % num)
f.close()


# file.readline读取单独一行，如果返回一个空字符串，说明已经读到最后一行
print('readline'.center(30, '*'))
f = open('../others/abc.txt', 'r')
str2 = f.readline()
print(str2)
f.close()

# file.read(size)是读取一定数量的数据，size被忽略或者为负时，该文件的所有内容都将被读取并且返回
print('read'.center(30, '*'))
f = open('../others/abc.txt', 'r')
str3 = f.read()
print(str3)
f.close()

# file.readlines返回一个列表，列表的每一个元素是一行数据，如果设置可选参数sizehint则读取指定长度的字节，但至少读取一行
print('readlines'.center(30, '*'))
f = open('../others/abc.txt', 'r')
str4 = f.readlines()
print(str4)
f.close()


# file.tell()返回文件对象当前所处的位置，它是从文件开头开始算起的字节数
print('f.tell()'.center(30, '*'))
f = open('../others/abc.txt', 'r')
str5 = f.read(10)
num = f.tell()
print('读取的{}个字节为{}'.format(num, str5))
f.close()


# file.seek(offset, from_what)可以改变文件当前的位置
# seek(x,0)从起始位置开始移动x个字符,from_what忽略时即从起始位置
# seek(x,1)从当前位置开始移动y个字符
# seek(-x,2)从文件结尾往前移动x个字符
print('f.seek'.center(30, '*'))
f = open('../others/abc.txt', 'r')
f.seek(10, 0)
str6 = f.readline()
print(str6)
