## 数据结构
- 1. 从字典中取值，若不存在，则返回0
```py
Dict =  {"1":1,"4":2, "8":5}
Dict.get(num, 0)
```
- 2. python3 get max int
```py
import sys
max = sys.maxsize
```
- 3. python3 get max float
```py
import sys, max = sys.float_info.max
infinity = float("inf")
```
- 4. get the max value's key from a dict
```py
d = {"a":1,"b":2, "c":5}
max(d, key=lambda k: d[k]) # solution 1,
max(d, key=d.get)          # solution 2,
max(d.items(), key=operator.itemgetter(1))[0] # solution 3, not easy understanding, not recomended,
max("adfasf", "wrwessd", "sa", key=len) # get the string with max length,from problem 005 py_2,
```
- 5. return default value if key is not in the dict
```py
d = {"a":1,"b":2, "c":5}
local_int = d.get('f',10)   # dict.get(key,default)
```

## 常用库函数
- 1. 将 list 转化为 小顶堆
```py
import heapq
nums = [4,5,8,2]
heapq.heapify(nums)
```
- 2. 小顶堆常用操作
```py
heappush(heap, x)                                              #将x压入堆中
heappop(heap)                                                  #从堆中弹出最小的元素
heapify(heap)                                                  #让列表具备堆特征
x = heapreplace(heap, x)                                       #弹出最小的元素，并将x压入堆中
list_x = nlargest(n, iter)                                     #返回iter中n个最大的元素
list_x = nsmallest(n, iter)                                    #返回iter中n个最小的元素
```
- 3. 对 list 的元素计数，并返回每个元素及其出现个数的字典对象
```py
import collections
nums = [4,5,8,2]
counts = collections.Counter(nums)
```
- 4. 对 prices 的每个元素，若前一个元素小于后一个，则用后一个元素减去前一个，直到最后一个元素，再全部求和
```py
# from 无限次股票买卖问题
prices = [4,5,8,2]
sum([y - x for x, y in zip(prices[:-1], prices[1:]) if x < y])
sum(max(b-a,0)for a,b in zip(prices,prices[1:]))
```
- 5. special handle for the 1st row and 1st col of a 2D matrix combined in the loop, refer to 1329 xxx_3.py
```py
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            #combine the sort(i,0) and sort(0,j) with 2 nested loop and below if condition judgement.
            for j in range(1 if i else n):
                rj = zip(mat[i:], range(j, n))
                vals = iter(sorted(r[j] for r, j in rj))                
```
- 6. map 函数
```py
def square(x) :
    return x**2
map(square, [1,2,3,4,5]) # [1, 4, 9, 16, 25]
map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10]) # [3, 7, 11, 15, 19]    
```
- 7. 多线程并发之Semaphore(信号量)，mutex（互斥量）
```py
from threading import Semaphore
self.m = Semaphore(1) # No.1279, Traffic_Light_Controll
```
- - 7.1 semaphore（信号量）范围比较广，semaphore可能会有多个属性值。比如常见的生产者和消费者问题，就是多元信号量的一种。生产者可以生产多个元素，消费者可以消费的元素必须小于生产者的生产元素个数。从此也可以看出，semaphore是允许多个线程进入，访问互斥资源。除了多元信号量之外，还存在一种二元信号量。即只存在是与否，0与1两种状态。
- - 7.2 mutex（互斥量）也是一种二元的锁机制，只有是（1）和否（0）的两个值，和二元信号量比较相似。但是它和二元信号量不同的是，占有和释放必须是同一个线程。比如互斥量M被线程A占有，那么释放的时候肯定也是A线程释放的。二元信号量则不必如此，一个二元信号量的占有和释放可以是不同线程
- 8. 多线程
```py
import threading
def worker(sign, lock):
    lock.acquire()
    print(sign, os.getpid())
    lock.release()
lock = threading.Lock()
thread = threading.Thread(target=worker, args=('thread', lock))
thread.start()   
```
- 9. 多进程
```py
import multiprocessing
def worker(sign, lock):
    lock.acquire()
    print(sign, os.getpid())
    lock.release()
lock = multiprocessing.Lock()
process = multiprocessing.Process(target=worker, args=('process', lock))
process.start()
```
- 10. collections.defaultdict()的使用
```py
from collections import defaultdict 
s=[('yellow',1),('blue', 2), ('yellow', 3), ('red', 1)]
d=defaultdict(list)     # No.49
for k, v in s:
    d[k].append(v)
a=sorted(d.items())
```
- 11. reduce的用法
```py
# No.171, xx_2.py,
# reduce(function, sequence[, initial]) -> value
# 对sequence连续使用function, 如果不给出initial, 则第一次调用传递sequence的两个元素, 以后把前一次调用的结果和sequence的下一个元素传递给function.
# 如果给出initial, 则第一次传递initial和sequence的第一个元素给function.
from functools import reduce 
res = reduce(lambda x, y: x+y, [1,2,3], 9) 
# res = 9 + ((1+2)+3) = 15
```
- 12. Python3字符串拼接的几种方法
```py
'wbz' + 'ctt' ='wbzctt' # 12.1, str1 + str2
'wbz','ctt' =('wbz','ctt') # 12.2, str1,str2
'wbz' 'ctt'='wbzctt' # 12.3, str1 str2
'%s %s' % ('wbz','ctt') = 'wbz ctt'  # 12.4, %连接字符串
#  12.5, str.join(list) 
data = ['wbz','ctt','Python']
str1 = '@@@'  
str2 = ''
str1.join(data) = 'wbz@@@ctt@@@Python'
str2.join(data) = 'wbzcttPython'
str = "-" 
seq = ("a", "b", "c")  # 字符串序列
print str.join( seq )  # a-b-c, used in No.71
# 12.6, 字符串乘法
str1 = 'Python'
str1 * 2 = 'PythonPython'
```
- 13. 数值元素的list转字符串并去除左侧的'0'
```py
nums = [0,0,0,2,4,6,9]
res = "".join(finalStack).lstrip('0')  # used in No.402
```