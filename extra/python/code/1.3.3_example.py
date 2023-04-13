name = ['shi', 'li', 'wang', 'zhao']
print(f"排序后：{sorted(name)}\n 排序前：{name}")
name.sort()
print(name)
name.sort(reverse=True) 
print(f"这是反转了一次{name}")
name.reverse
print(f"又反转了一次{name}")
"""
输出结果为：
排序后：['li', 'shi', 'wang', 'zhao']
 排序前：['shi', 'li', 'wang', 'zhao']
['li', 'shi', 'wang', 'zhao']
这是反转了一次['zhao', 'wang', 'shi', 'li']
又反转了一次['zhao', 'wang', 'shi', 'li']
"""