
class Node:
     def __init__(self, value):
          self._value = value
          self._next =  None

class LinkedList:
     def __init__(self):
          self._head = None

     def insertOnFirst(self, value):
          new_node = Node(value)
          new_node._next = self._head
          self._head = new_node

     def insertOnLast(self, value):
          new_node = Node(value)
          if self._head is None:
               self._head = new_node
          else:
               temp = self._head
               while temp._next != None:
                    temp = temp._next
               temp._next = new_node
               

     def insertOnMiddle(self, value, x):
          n = self._head
          while n is not None:
               if x == n._value:
                    break
               n = n._next
          if n is None:
               print("Node is not present")
          else:
               new_node = Node(value)
               new_node._next = n._next
               n._next = new_node

     def deleteFromFirst(self):
          if self._head is None:
               print("Linked List is Empty")
          else:
               self._head = self._head._next

     def deleteFromLast(self):
          if self._head is None:
               print("Linked List is Empty")
          else:
               temp = self._head
               while temp._next._next is not None:
                    temp = temp._next
               temp._next = None


     def deleteFromMiddle(self, x):
          n = self._head
          while n is not None:
               if x == n._next._value:
                    break
               n = n._next
          if n._next is None:
               print("Node is not present")
          else:
               n._next = n._next._next

     def display(self):
          if self._head is None:
               print("Linked list is empty")
          else:
               temp = self._head
               while temp is not None:
                    print(temp._value)
                    temp = temp._next

LL1 = LinkedList()
# LL1.insertOnFirst(3)
LL1.insertOnLast(3)
LL1.insertOnLast(4)
LL1.insertOnLast(5)
LL1.insertOnMiddle(9, 4)
LL1.insertOnMiddle(6, 9)
# LL1.deleteFromFirst()
# LL1.deleteFromLast()
LL1.deleteFromMiddle(9)
LL1.deleteFromMiddle(6)
LL1.display()

