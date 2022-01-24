from functools import *
n = int(input())
num = input()
num_lst = list(num)
int_lst = list(map(int,num_lst))
sum_num = sum(int_lst)
prod_num = reduce(lambda x,y:x*y,int_lst)
print(abs(sum_num - prod_num))
