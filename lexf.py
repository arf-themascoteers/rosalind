dataset = """A B C D E
4"""


def perm(mylist, length):
    if length == 1:
        return mylist
    returnListString = list()
    for i in mylist:
        result = perm(mylist, length-1)
        returnListString.extend([i+item for item in result])
    return returnListString


lines = dataset.splitlines()
alphabet = lines[0].strip().split(" ")
length = int(lines[1].strip())
result = perm(alphabet, length)
print("\n".join(result))
