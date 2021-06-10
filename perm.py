def perm(mylist):
    if len(mylist) == 1:
        return str(mylist[0])
    returnListString = list()
    for i in mylist:
        newList = mylist.copy()
        newList.remove(i)
        result = perm(newList)
        returnListString.extend([str(i)+ item for item in result])
    return returnListString

n = 5
result = perm(list(range(1,n+1)))
print(len(result))
print("\n".join([" ".join(r) for r in result]))
