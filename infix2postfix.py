def flatten(lst):
    flat_list = []
    for sublist in lst:
        if isinstance(sublist, list):
            flat_list.extend(flatten(sublist))
        else:
            flat_list.append(sublist)
    return flat_list

def precdict_conversion(lst):
     indexed_precedence = {}
     for i, sublist in enumerate(lst):
          indexed_precedence[i] = sublist
     
     return indexed_precedence

class Infix2Postfix:
     def __init__(self, INFIX_EXPR):
          self._INFIX_EXPR = INFIX_EXPR
          self._INFIX_LIST = list(self._INFIX_EXPR)
          self._stack = []
          self._output = []
          self._top = -1
          self._INFIX_LIST.insert(0, "(")
          self._INFIX_LIST.append(")")
          self._MAX_SIZE = len(self._INFIX_LIST)
     
     def isOperator(self, op):
          if op == "+" or op == "-" or op == "*" or op == "/" or op == "^":
               return True
          else: 
               return False
          
     def precedence(self, op):
          if op == "^":
               return 3
          if op == "/" or op == "*":
               return 2
          if op == "+" or op == "-":
               return 1
          else: 
               return -1

     def push(self, OPR):
          # self.stack_overflow()
          self._top += 1
          self._stack.append(OPR)
     
     def pop(self):
          # self.stack_underflow()
          self._top -= 1
          self._stack.pop()

     def process(self):
          for idx, var_cache in enumerate(self._INFIX_LIST):
               if var_cache.isalpha():
                    self._output.append(var_cache)

               elif var_cache == '(':
                    self.push(var_cache)

               elif var_cache == ')':
                    while self._stack[self._top] != "(" and len(self._stack) != 0:
                         self._output.append(self._stack[self._top])
                         self.pop()
                    if self._stack[self._top] == "(":
                         self.pop()

               elif self.isOperator(var_cache):
                    if self._top == -1:
                         self.push(var_cache)
                    else:
                         if self.precedence(var_cache) >= self.precedence(self._stack[self._top]):
                              self.push(var_cache)
                         else:
                              while self.precedence(var_cache) < self.precedence(self._stack[self._top]):
                                   self._output.append(self._stack[self._top])
                                   self.pop()

                              if self.precedence(var_cache) >= self.precedence(self._stack[self._top]):
                                   self.push(var_cache)
          
     def display(self):
          return self._output

if __name__ == '__main__':
     Obj = Infix2Postfix("A+B*C-D/(E+F)^G")
     Obj.process()
     print(Obj.display())
