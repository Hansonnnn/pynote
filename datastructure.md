#### 迭代解压

##### 解压序列赋值给多个变量

* 多个变量按顺序赋值
```
    p = (3,4)
    x,y = p

```
* 部分变量赋值，使用占位符
```
   data = ['ACME', 50, 91.1, (2012, 12, 21)]
  
 _, shares, price, _ = data
```
* 使用星号符去除最高和最低分

```

def drop_first_last():
    grades = [7,8,10,10,10,10,10,9,10]
    first, *middle, last = grades
    print(first,middle,last)

result :7 [8, 10, 10, 10, 10, 10, 9] 10

```
* 使用星号符迭代可变长元组序列（未知长度）

```
def kv():

    records = [('foo', 1, 2),
               ('bar', 'hello'),
               ('foo', 3, 4), ]


    def do_foo(x, y): print('foo', x, y)


    def do_bar(s): print('bar', s)


    for tag, *args in records:
        if tag == 'foo':
           do_foo(*args)
        elif tag == 'bar':
           do_bar(*args)

result:foo 1 2
       bar hello
       foo 3 4
```
#### 保留最后N个元素

示例：返回在前N行中匹配成功的行

```
from collections import deque

def search(lines, pattern, history=5): 
previous_lines = deque(maxlen=history) 
for li in lines:
    if pattern in li:
      yield li, previous_lines
    previous_lines.append(li)
# Example use on a file
if __name__ == '__main__':
with open(r'../../cookbook/somefile.txt') as f:

for line, prevlines in search(f, 'python', 5):
  for pline in prevlines:
    print(pline, end='')
    print(line, end='') 
    print('-' * 20)
```
#### 查找最大或最小的N个元素

问题：怎样从一个集合中获得最大或者最小的N个元素列表?

```
import heapq

def smallOrLarge():
    nums = [10,20,-10,-8,10,23,30,65,-1]
    print(heapq.nlargest(3,nums))
    print(heapq.nsmallest(3,nums))
```

#### 字典中的键映射多个值

怎样实现一个键对应多个值的字典?

使用defaultdict可以不用考虑使用字典时的细节，并且代码简洁，只需要关注字典元素的增加和删除。

```
from collections import defaultdict

default = {'shoe':1,'box':3,'another':10}
kv = defaultdict(list)

for key,value in default.items():
    kv[key].append(value)
```

#### 字典运算

对字典求最大最小或者排序。

求字典中的最大最小

```
prices = {
'ACME': 45.23,
'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75
}

min_price = min(zip(prices.values(),prices.keys()))
max_price = max(zip(prices.values(),prices.keys()))
```
zip()是用来在对字典计算之前对字典的key、value进行反转。

对字典排序

```
sorted_price = sorted(zip(prices.values(),prices.keys()))
```
 zip()函数方案通过将字典”反转”为(值，键)元组序列来简短完成字典的比较以及排序。当比较 两个元组的时候，值会先进行比较，然后才是键。

>注意：需要注意的是在计算操作中使用到了(值，键)对。当多个实体拥有相同的值的时候，键会 决定返回结果。 比如，在执行 和 操作的时候，如果恰巧最小或最大值有重 复的，那么拥有最小或最大键的实体会返回。

如下示例：

```
prices_1 = {
    'AAA':43.1,'DDD':43.1
}

print(min(zip(prices_1.values(),prices_1.keys())))
print(max(zip(prices_1.values(),prices_1.keys())))

```
```
(43.1, 'AAA')
(43.1, 'DDD')
```

#### 序列中出现次数最多的元素

怎样找出一个序列中出现次数最多的元素呢?

使用collection包中的Counter模块，并且在Counter模块中有准备most_common()函数用来得出集合中出现频率top n的元素。

```
from collections import Counter

words = [
'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into', 'my', 'eyes', "you're", 'under'
]
words_count = Counter(words)

top_n = words_count.most_common(3)

print(top_n)
```

Counter可以使用任意的hashable序列对象，在底层实现上Counter使用了字典结构存储，映射元素与其在序列中出现频率。





 



:q
