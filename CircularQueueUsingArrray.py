
class CircularQueue:
     def __init__(self, MAX_SIZE):
          self._MAX_SIZE = MAX_SIZE
          self._rear = -1
          self._front = -1
          self._array = [None] * self._MAX_SIZE
     
     def isEmpty(self):
          if self._rear == -1 and self._front == -1:
               return True
          else:
               return False

     def isFull(self):
          if (self._rear + 1)%self._MAX_SIZE == self._front:
               return True
          else:
               return False

     def insert(self, num):
          if self.isFull() == False:

               if self._front == -1 and self._rear == -1:
                    self._front = 0
                    self._rear = 0
                    self._array[self._rear] = num
               else:
                    self._rear = (self._rear + 1)%self._MAX_SIZE
                    self._array[self._rear] = num
          else:
               print("Queue Overflow.") 

     def delete(self):
          if self.isEmpty() == False:
               if self._front == self._rear:
                    print(self._array[self._front], "=> Deleted Successfully")
                    self._array[self._front] = None
                    self._front = self._rear = -1

               else:
                    print(self._array[self._front], "=> Deleted Successfully")
                    self._array[self._front] = None
                    self._front = (self._front+1)%self._MAX_SIZE

          else:
               print("Queue is already Empty")

     def display(self):
          print("Array: ", self._array)

     def pointer(self):
          print("front=>",self._front)
          print("rear=>",self._rear)

if __name__ == "__main__":
     Obj = CircularQueue(5)
     Obj.insert(2)
     Obj.pointer()
     Obj.display()
     print("****************************")
     Obj.insert(6)
     Obj.pointer()
     Obj.display()
     print("****************************")
     Obj.insert(8)
     Obj.pointer()
     Obj.display()
     print("****************************")
     Obj.delete()
     Obj.pointer()
     Obj.display()
     print("****************************")
     Obj.delete()
     Obj.pointer()
     Obj.display()
     print("****************************")
     Obj.insert(4)
     Obj.pointer()
     Obj.display()
     print("****************************")
     Obj.insert(9)
     Obj.pointer()
     Obj.display()
     print("****************************")
     Obj.insert(10)
     Obj.pointer()
     Obj.display()
     print("****************************")
     Obj.delete()
     Obj.pointer()
     Obj.display()
     print("****************************")
     Obj.insert(11)
     Obj.pointer()
     Obj.display()
     print("****************************")
     Obj.insert(12)
     Obj.pointer()
     Obj.display()
     print("****************************")
     Obj.insert(12)
     Obj.pointer()
     Obj.display()