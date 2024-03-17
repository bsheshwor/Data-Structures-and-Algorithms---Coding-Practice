class StackArray:
     def __init__(self, MAX_SIZE):
          self._stack_list = []
          self._MAX_SIZE = MAX_SIZE
          self._top = -1

     def is_empty(self):
          if len(self._stack_list) < 0:
               raise Exception("Empty List")

     def stack_overflow(self):
          if len(self._stack_list) > self._MAX_SIZE:
               return Exception("Stack Overflow")
     
     def stack_underflow(self):
          if len(self._stack_list) <= 0:
               return Exception("Stack Underflow")

     def push(self, num):
          self.stack_overflow()
          self._stack_list.append(num)
          self._top += 1
     
     def pop(self):
          self.stack_underflow()
          self._stack_list.pop()
          self._top -= 1

     def display(self):
          return self._stack_list
     
     def top(self):
          return self._top

if __name__ == '__main__':
     Obj = StackArray(5)
     Obj.is_empty()
     Obj.push(5)
     print(Obj.display())
     print(Obj.top())
     Obj.push(4)
     print(Obj.display())
     print(Obj.top())
     Obj.push(3)
     print(Obj.display())
     print(Obj.top())
     Obj.push(1)
     print(Obj.display())
     print(Obj.top())
     Obj.push(2)
     print(Obj.display())
     print(Obj.top())
     # Obj.push(6)
     Obj.pop()
     print(Obj.display())
     print(Obj.top())
     Obj.pop()
     print(Obj.display())
     print(Obj.top())
     Obj.pop()
     print(Obj.display())
     print(Obj.top())
     Obj.pop()
     print(Obj.display())
     print(Obj.top())
     Obj.pop()
     print(Obj.display())
     print(Obj.top())
     Obj.pop()