import sys
n = int(sys.stdin.readline())
btree = {}
for _ in range(n):
    parent, left, right = sys.stdin.readline().split()
    btree[parent] = [left,right]
    
def pre_order(start):
    if start != '.':
        print(start, end = '')
        pre_order(btree[start][0])
        pre_order(btree[start][1])
        
def in_order(start):
    if start != '.':
        in_order(btree[start][0])
        print(start, end = '')
        in_order(btree[start][1])
        
def post_order(start):
    if start != '.':
        post_order(btree[start][0])
        post_order(btree[start][1])
        print(start, end = '')

pre_order('A')
print()
in_order('A')
print()
post_order('A')
    
