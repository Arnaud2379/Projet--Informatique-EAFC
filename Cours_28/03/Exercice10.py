
def foo2(x):
    if x > 0 and x%2 ==0 and x%3 != 0 and x%4 != 0 :
        return True
    else:
        return False
print(foo2(-20))
print(foo2(10))
print(foo2(16))
print(foo2(30))