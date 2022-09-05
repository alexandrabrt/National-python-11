stackList = []


def push(val):
    stackList.append(val)


push(3)
push(2)
push(1)
print(stackList)


def pop():
    valoare = stackList[-1]
    del stackList[-1]
    return valoare


print(pop())
print(pop())
print(pop())
