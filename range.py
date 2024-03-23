with open('workfile', 'wb') as f:
    f.write(b'0123456789abcdef')
f = open('workfile', 'rb+')
f.seek(5)
print(f.read(1))
f.close()


# try:
#     open("database.sqlite")
# except OSError:
#     raise RuntimeError("unable to handle error")

# def bool_return():
#     try:
#         print("true from TRUE")
#         return True
#     finally:
#         print("flase fro FALSE")
#         return False
    
# print(bool_return())    

class TestClass:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y   = y
    def my_method(self):
        print('calling from my_method')    

print(f'type(TestClass.my_method) is: {type(TestClass.my_method)}')
print(f'TestClass.my_method: is {TestClass.my_method}')

instance = TestClass(5,5)
print(f'instanciated of TestClass.my_method is : {instance.my_method}')