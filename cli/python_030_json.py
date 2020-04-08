# coding=utf-8
import json

'''
json.dumps 将Python对象编码成json数据
json.loads 将已编码的json数据解码成Python对象

json.dump 将Python对象编码成json数据并存入文件
json.load 从文件中读取json数据并解码成Python对象
'''

# 字典转换为json字符串
dict1 = {
    'no' : 1,
    'name' : '百度',
    'url' : 'http://www.baidu.com'
}

json_str = json.dumps(dict1)
print(repr(json_str))

# json字符串转换为字典
dict2 = json.loads(json_str)
print(type(dict2))
print(dict2)

with open('../others/demo.json', 'w') as f:
    json.dump(dict1, f)
    print('保存成功')

with open('../others/menu.json', 'r') as f:
    dict3 = json.load(f)
    print(dict3)
    print(type(dict3))
    print('读取成功')
