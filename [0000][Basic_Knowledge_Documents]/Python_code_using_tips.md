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