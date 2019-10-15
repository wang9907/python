import sys
list = [1,2,3,4]
it = iter(list)
print(next(it))
print(next(it))

for x in it:
    print(x,end=",")

class myNumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <20:
            x = self.a
            self.a +=10
            return x
        else:
            raise StopIteration
myclass = myNumbers()
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))

def fibonacci(n): #生成器函数- - 斐波那契
    a,b,counter = 0,1,0
    while True:
        if(counter >n):
            return
        yield a
        a,b = b,a+b
        counter+=1
f = fibonacci(10) #f 是一个迭代器，由生成器返回生成
while True:
    try:
        print(next(f),end=" ")
    except StopIteration:
        sys.exit()
