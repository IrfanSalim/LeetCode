#
# @lc app=leetcode id=146 lang=python
#
# [146] LRU Cache
#

# @lc code=start
class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cacheMap = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cacheMap:
            temp = self.cacheMap[key]
            self.remove(temp)
            self.insert(temp)
            return temp.val
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        new = Node(key, value)
        if key in self.cacheMap:
            self.remove(self.cacheMap[key])
            del self.cacheMap[key]
        elif len(self.cacheMap) == self.cap:
            del self.cacheMap[self.head.next.key]
            self.remove(self.head.next)
        self.insert(new)
        self.cacheMap[key] = new
            
    def remove(self, node):
        t1 = node.prev
        t2 = node.next
        t1.next = t2
        t2.prev = t1
        node.prev, node.next = None, None

    def insert(self, node):
        t1 = self.tail.prev
        t1.next = node
        node.prev = t1
        node.next = self.tail
        self.tail.prev = node
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

