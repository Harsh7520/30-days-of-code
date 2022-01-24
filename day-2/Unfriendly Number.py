def checkdup(lst):
    if len(lst) == len(set(lst)):
        return False
    else:
        return True

lst = list(map(int,input()))
boolE = checkdup(lst)
if(boolE==True):
    print("The number is unlucky.")
else:
    print("The number is lucky.")
