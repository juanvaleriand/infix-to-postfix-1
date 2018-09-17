def operator(op1):
   if op1 == "^":
      return 4
   elif op1 == "*" or op1 == "/":
      return 3
   elif op1 == "+" or op1 == "-":
      return 2
   elif op1 == "(":
      return 1
   
   
def infix_to_postfix(infix_expr):
   infix_lists = infix_expr.split()
   postfix = []
   stack = []
   print("Stack","\t   ","Postfix")
   for infix in infix_lists:
      if infix == "(":
         stack.insert(0, infix)
      elif infix == ")":
         top_stack = stack.pop(0)
         while top_stack != "(":
            postfix.append(top_stack)
            top_stack = stack.pop(0)
      elif infix == "^" or infix == "*" or infix == "/" or infix == "+" or infix == "-":
         while (not stack == []) and (operator(stack[0]) >= operator(infix)):
            postfix.append(stack.pop(0))
         stack.insert(0, infix)
      else:
         postfix.append(infix)
      print(" ".join(stack),"\t   "," ".join(postfix))
   print()
   print("Postfix : ",end = " ")
   while not stack == []:
      postfix.append(stack.pop(0))
   print(" ".join(postfix))
   
masukkan_infix = input("Infix : ")
infix_to_postfix(masukkan_infix)


   
   
