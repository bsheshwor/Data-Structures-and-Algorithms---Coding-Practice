
class Queue:
     def __init__(self, MAX_SIZE):
          self._MAX_SIZE = MAX_SIZE
          self._rear = -1
          self._front = -1
          self._array = []
     
     def isEmpty(self):
          if self._rear == -1 and self._front == -1:
               return True
          else:
               return False

     def isFull(self):
          if self._rear == (self._MAX_SIZE - 1):
               return True
          else:
               return False

     def insert(self, num):
          if self.isFull() == False:
               self._array.append(num)
               self._rear += 1

               if self._front == -1:
                    self._front = 0
          else:
               print("MAX SIZE Exceeded.") 

     def delete(self):
          if self.isEmpty() == False:
               if self._front == self._rear and self._front == self._MAX_SIZE-1:
                    print(self._array[self._front], "=> Deleted Successfully")
                    self._array[self._front] = None
                    self._front = self._rear = -1

               else:
                    print(self._array[self._front], "=> Deleted Successfully")
                    self._array[self._front] = None
                    self._front += 1
                    if self._front >  self._rear:
                         self._front = self._rear = -1
                         self._array = []

          else:
               print("Queue is already Empty")

     def display(self):
          print("Array: ", self._array)

     def pointer(self):
          print("rear=>",self._rear)
          print("front=>",self._front)

if __name__ == "__main__":
     Obj = Queue(5)
     Obj.insert(2)
     Obj.pointer()
     Obj.display()
     Obj.insert(6)
     Obj.pointer()
     Obj.display()
     Obj.insert(8)
     Obj.pointer()
     Obj.display()
     Obj.delete()
     Obj.pointer()
     Obj.display()
     Obj.delete()
     Obj.pointer()
     Obj.display()
     Obj.insert(4)
     Obj.pointer()
     Obj.display()
     Obj.insert(9)
     Obj.pointer()
     Obj.display()
     Obj.delete()
     Obj.pointer()
     Obj.display()
