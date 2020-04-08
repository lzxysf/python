'''
time提供了time和calendar模块来格式化日期和时间
'''
import time
import calendar

# 当前时间戳
ticks = time.time()
print('当前时间戳为:', ticks)

# 时间戳→时间元组
localtime = time.localtime(time.time())
print(localtime)

# 时间戳→可视化时间
ctime = time.ctime(time.time())
print(ctime)

# 时间元组→可视化时间
asctime = time.asctime(time.localtime(time.time()))
print(asctime)

# 时间元组→可视化时间（定制）
time1 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
print(time1)    # 结果为 2019-05-30 16:06:05

# 可视化时间→时间元组
structtime = time.strptime('2019-05-30 15:52:44', '%Y-%m-%d %H:%M:%S')
print(structtime)


# time.perf_counter()
# 返回计时器的精准计时（系统的运行时间），包含整个系统的睡眠时间。由于返回值的基准点是未定，所以只有连续调用的结果之间的差值才是有用的
time1 = time.perf_counter()
time.sleep(1)
time2 = time.perf_counter()
print(time1)
print(time2)
run_time = time2 - time1
print('这之间代码的运行时间', run_time)

# time.process_time()
# 返回当前进程执行CPU的时间总和，不包含睡眠时间。由于返回值的基准点是未定，所以只有连续调用的结果之间的差值才是有用的
time3 = time.process_time()
time.sleep(1)
time4 = time.process_time()
run_time = time4 - time3
print('运行时间', run_time)



cal = calendar.month(2019, 5)
print(cal)
