# 相较于静态语言，动态语言可以动态创建属性和方法，因此是不严谨的
# 可以使用__slots__对其进行限制
# 注意，slots仅对当前类实例有效，对子类是不起作用的


class Person():
    __slots__ = ("name", "age")


p = Person()
p.name = '老王'
p.age = 20
# p.score = 100 # 执行此句后报错，即此类已经被限制只能定义name和age属性，不能添加其它属性
