# p=0
# c=1
# for i in range(8):
#     pp=p
#     p=c
#     c=pp+p
#     print(c)
p=0
c=1
def pal(n):
    global p
    global c
    if c>=n:
       print(c)
    else:

       pp = p
       p = c
       c = pp + p
       print(c)
       pal(n)
pal(5)