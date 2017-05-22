my_list=['dara','sok','sopheak']
# for e in  my_list:
#     print(e)

# for e in my_list:
#     if 'sokha' in my_list:
#         print 'Found sopheak'
#         break
#     else:
#         print(e)
def f(a,L=None):
    if L is None:
        L=[]
    L.append(a)
    return L

print f(1),f(2),f(1,[3,4])
