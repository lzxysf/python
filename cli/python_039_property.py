# 私有属性添加getter和setter方法
class Money:
    def __init__(self):
        self.__money = 0

    def getMoney(self):
        return self.__money

    def setMoney(self, money):
        if isinstance(money, int):
            self.__money = money
        else:
            print('输入的不是整数')


m = Money()
m.setMoney(100)
# print(m.__money) 私有属性外部无法访问
print(m.getMoney())


# 使用property改造getter和setter方法
class Money:
    def __init__(self):
        self.__money = 0

    def getMoney(self):
        return self.__money

    def setMoney(self, money):
        if isinstance(money, int):
            self.__money = money
        else:
            print('输入的不是整数')

    money = property(getMoney, setMoney)


m = Money()
m.money = 122
print(m.money)


# 使用@property取代getter和setter用法
class Money:
    def __init__(self):
        self.__money = 0

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, value):
        if isinstance(value, int):
            self.__money = value
        else:
            print('输入的不是整数')


m = Money()
m.money = 102
print(m.money)
