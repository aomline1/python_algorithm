#a=[i for i in range(1,10) if i>3]
#g=filter(lambda x:x>7,a) print(next(g)) 8 print(list(g))

#为元祖元素命名，提高可读性
# student=('jim',16,'male')
# from enum import IntEnum#print(student[Studentenum.NAME])
# class Studentenum(IntEnum):
#      NAME, AGE, SEX = range(3)
#
# from collections import namedtuple#print(s2[name])
# st=namedtuple('student',['name','age','sex'])
# s2=st('jim',16,'male')

#对字典的项排序
# from random import randint
# d={k:randint(20,40) for k in "adghy"}
# # l=[(v,k) for k,v in d.items()]
# # print(sorted(l))
# # print(list(zip([1,2,3],[4,5,6])))  [(1, 4), (2, 5), (3, 6)]
# # print(sorted(list(zip(d.values(),d.keys()))))
# print(sorted(d.items(),key=lambda x:x[1]))
# print(list(enumerate([1,2,3],2)))

#统计序列的频率
from random import randint,sample
# a=[randint(0,20) for _ in range(30)]
# d=dict.fromkeys(a,0)
# for x in a:
#     d[x]+=1
# print(sorted(((v,k) for k,v in d.items()),reverse=True)[:3])
#
# import heapq
# print(heapq.nlargest(3,((v,k) for k,v in d.items())))
#
# from collections import Counter
# c=Counter(a)
# print(c.most_common(3))

#查找多个字典公共key
# a={k:randint(1,4) for k in sample("abcdefgh",randint(3,6))}
# b={k:randint(1,4) for k in sample("abcdefgh",randint(3,6))}
# c={k:randint(1,4) for k in sample("abcdefgh",randint(3,6))}
# d=[a,b,c]
# print([k for k in d[0] if all(map(lambda d:k in d,d[1:]))])
# from functools import reduce
# print(reduce(lambda a,b:a*b,range(1,11)))
# print(reduce(lambda a,b:a&b,map(dict.keys,d)))