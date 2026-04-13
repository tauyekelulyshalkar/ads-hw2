'''
def m_e(nums):
    max_count = 0
    result = None

    for x in nums:
        count = nums.count(x)
        if count > max_count:
            max_count = count
            result = x

    return result

print(m_e([2,1,1,2,3,2,2,3,3,2]))
'''

'''
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def middle_node(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.val

a = list(map(int, input().split()))

head = ListNode(a[0])
cur = head
for x in a[1:]:
    cur.next = ListNode(x)
    cur = cur.next

print(middle_node(head))
'''

'''
a = list(map(int, input().split()))
a.sort()
print(*a)
'''

'''
from collections import deque

q = deque()

n = int(input())

for _ in range(n):
    s = input().split()

    if s[0] == "push":
        q.append(int(s[1]))
    elif s[0] == "pop":
        if q:
            print(q.pop())
'''

'''
s = input()
t = input()

map1 = {}
map2 = {}

ok = True

for i in range(len(s)):
    c1 = s[i]
    c2 = t[i]

    if c1 in map1 and map1[c1] != c2:
        ok = False
    if c2 in map2 and map2[c2] != c1:
        ok = False

    map1[c1] = c2
    map2[c2] = c1

print(ok)
'''

'''
'''


from collections import Counter

a = list(map(int, input().split()))
k = int(input())

c = Counter(a)
res = c.most_common(k)

print(*[x for x, _ in res])

