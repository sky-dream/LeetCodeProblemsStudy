# -*- coding: utf-8 -*-  
# leetcode time     cost : 244 ms
# leetcode memory   cost : 22.4 MB
# Time  Complexity: O(1)
# Space Complexity: O(capacity)
# solution 2, hash table and double linked list,
class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        # 新建两个节点 head 和 tail
        self.head = ListNode()
        self.tail = ListNode()
        # 初始化链表为 head <-> tail
        self.head.next = self.tail
        self.tail.prev = self.head

    # 因为get与put操作都可能需要将双向链表中的某个节点移到头部(变成最新访问的)，所以定义一个方法
    def move_node_to_header(self, key):
            # 先将哈希表key指向的节点拎出来，为了简洁起名node
            #      hashmap[key]                               hashmap[key]
            #           |                                          |
            #           V              -->                         V
            # prev <-> node <-> next         pre <-> next   ...   node
            node = self.hashmap[key]
            node.prev.next = node.next
            node.next.prev = node.prev
            # 之后将node插入到头部节点前
            #                   hashmap[key]                     hashmap[key]
            #                       |                                 |
            #                       V        -->                      V
            # header <-> next  ... node                   header <-> node <-> next
            node.prev = self.head
            node.next = self.head.next
            self.head.next.prev = node
            self.head.next = node
            
    def add_node_to_header(self, key,value):
        new = ListNode(key, value)
        self.hashmap[key] = new
        new.prev = self.head
        new.next = self.head.next
        self.head.next.prev = new
        self.head.next = new
        
    def pop_tail(self):
        last_node = self.tail.prev
        # 去掉链表尾部的节点在哈希表的对应项
        self.hashmap.pop(last_node.key)
        # 去掉最久没有被访问过的节点，即尾部Tail之前的一个节点
        last_node.prev.next = self.tail
        self.tail.prev = last_node.prev
        return last_node
    
    def get(self, key: int) -> int:
        if key in self.hashmap:
            # 如果已经在链表中了久把它移到头部（变成最新访问的）
            self.move_node_to_header(key)
        res = self.hashmap.get(key, -1)
        if res == -1:
            return res
        else:
            return res.value

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            # 如果key本身已经在哈希表中了就不需要在链表中加入新的节点
            # 但是需要更新字典该值对应节点的value
            self.hashmap[key].value = value
            # 之后将该节点移到链表头部
            self.move_node_to_header(key)
        else:
            if len(self.hashmap) >= self.capacity:
            # 若cache容量已满，删除cache中最不常用的节点 
                self.pop_tail()
            self.add_node_to_header(key,value)

# Your LRUCache object will be instantiated and called as such:
capacity = 2
cache = LRUCache(capacity)
cache.put(1, 1)
cache.put(2, 2)
param_1 = cache.get(1)          # returns 1
print(param_1)
cache.put(3, 3)                 # evicts key 2
param_1 = cache.get(2)          # returns -1 (not found)
print(param_1)
cache.put(4, 4)                 # evicts key 1
param_1 = cache.get(1)          # returns -1 (not found)
print(param_1)
param_1 = cache.get(3)          # returns 3
print(param_1)
param_1 = cache.get(4)          # returns 4
print(param_1)