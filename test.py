# for  a   in  range(1,10):
#     for  b  in  range(1,a+1):
#
#         if  (a==3 and b==2) or  (a==4 and  b==2):
#
#             print("%s*%s=%.2f"%(a,b,a*b),end="  ")
#
#         print("%s*%s=%.2f" % (a, b, a * b), end=" ")
#
#     print()
# a=0
# b=1
# # for  n  in  range(10):
# #    a,b=b,a+b
# #    print(a,b)
#
#
#
#
# # 第一个月  1
# # 第二个月  1
# # 第三个月  1*2=2   1
# #
# # 第四个月  1*2+1=2+1  1
# #
# # 第五个月  2*2+1=4+1  2
# # 第六个月  3*2+2=6+2  3
# #
# # 第七个月  5*2+3=13   5
# #
# # 第八个月
#
# while True:
#     a=0
#     b=1
#     try:
#         p=int(input(">>"))
#         if p<=0:
#             continue
#     except:
#         continue
#
#
#
#     if p<=1:
#         print(b*2)
#     else:
#         for  n  in  range(p):
#             if n==0 :
#                 a = 0
#                 b = 1
#             else:
#                 a,b=b,a+b
#         print(a*2)
# a="sadsadsafsadsafgyghr"
# n = 0
# list = []
# for b in a:
#     list.append((a.count(b),b))
#     n += 1
# print(list)
#
# for  c  in  range(len(list)):
#
#     for  m  in  range(c+1,len(list)):
#         if  list[c][0]>list[m][0]:
#             list[c],list[m]=list[m],list[c]
#
# for  p  in  list:
#
#     if p[0]>=list[-1][0]:
#         print(p[1])
#
# print(list[-1][1])



#
# def  count_set(args,parm):
#     n = 0
#     for m in args:
#         if m == parm:
#             n += 1
#     return n
#
# print(count_set("sadadfsafsadasdas","a"))
#
#
#
#
# a="56465417857875"
# a=list(a)
# print(a)
#
# a.sort()
# print(a)
#
# # print([m for m  in  range(int(n)+1,len(a)  for  n  in  range(len(a))])
#
# print(
#     "\n".join ( "\t".join( ["%s*%s=%s"%(x, y, x*y) for y in range(1, x + 1)] ) for x in range(1, 10)  ) )
#
# print([[y for y in range(1, x + 1)] for x in range(1, 10) ])

# a=1
# print(
#     "\n".join(
#         [ " ".join(["%s*%s=%s"%(a,b,a*b)   for  a  in  range(1,b+1)]) for  b  in  range(1,10)]
#     )
# )
#


import threading


class  Myt(threading.Thread):
    def __init__(self,args):
        super().__init__()
        self.args=args

    def  run(self):
        print(self.args)

if  __name__=="__main__":
    threads=[]
    t=Myt("你好吗")
    t1=Myt("很不好")
    threads.extend((t,t1))
    for  a  in  threads:
        a.start()




