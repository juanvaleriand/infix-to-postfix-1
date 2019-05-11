def operator(op1):
    if op1 == '^':
        return 3
    elif op1 == '*' or op1 == '/':
        return 2
    elif op1 == '+' or op1 == '-':
        return 1
    else:
        return 0

def len_terbesar(a_stack):
    terbesar = len(a_stack[0])
    for i in range(len(a_stack)):
        if len(a_stack[i]) > terbesar:
            terbesar = len(a_stack[i])
    return terbesar

def space(terbesar, stack):
    for i in range(len(stack)):
        loop = terbesar - len(stack[i])
        for looping in range(loop):
            stack[i].insert(0, ' ')
    return stack

def transpose_stck(space_stack):
    transpose_stack = []
    for i in range(len(space_stack[0])):
        temp_trsp = []
        for j in range(len(space_stack)):
            temp_trsp.append(space_stack[j][i])
        transpose_stack.append(temp_trsp)
    return transpose_stack

def cetak_stack(transpose_stack):
    text = "Stack: "
    for i in range(len(transpose_stack)):
        if i == 0:
            print(text, end="")
        else:
            print(' '*len(text), end="")
        for j in range(len(transpose_stack[0])):
            print(transpose_stack[i][j], end = " ")
        print()

def cetak_postfix(postfix):
    text = "Stack: "
    print(' '*len(text), end="")
    for i in postfix:
        print(i, end=' ')
    print()
    print()
    final_postfix(postfix)
     
def final_postfix(postfx):
    print("Postfix: ", end = "")
    for i in postfx:
        if i == '' or i == ' ':
            continue
        print(i, end = " ")
    print()
        
def proses_stack(arr_stack, len_stack, postfix):
    k = 0
    real_stack = []
    for i in range(len(len_stack)):
        temp_stack = []
        for j in range(len_stack[i]):
            temp_stack.append(arr_stack[k])
            k += 1
        real_stack.append(temp_stack)

    terbesar = len_terbesar(real_stack)        
    space_stack = space(terbesar, real_stack)
    transpose_stack = transpose_stck(space_stack)
    cetak_stack(transpose_stack)
    cetak_postfix(postfix)
     
  
def infix_to_postfix(infix_expr):
    infix_ex = list(infix_expr)
    postfix = []
    stack = []
    temp_stack = []
    len_stack = []
    print("Infix: ", end = "")
    for infix in infix_ex:
        if infix == ' ':
            continue
        elif infix == '(':
            stack.insert(0, infix)
            postfix.append(' ')
        elif infix == '^' or infix == '*' or infix == '/' or infix == '+' or infix == '-':
            while not stack == [] and operator(stack[0]) >= operator(infix):
                postfix.append(stack.pop(0))
            stack.insert(0, infix)
            postfix.append('')
        elif infix == ')':
            top_stack = stack.pop(0)
            while top_stack != '(':
                postfix.append(top_stack)
                top_stack = stack.pop(0)
        else:
            postfix.append(infix)
        temp_stack.extend(stack)
        len_stack.append(len(stack))
        print(infix, end = " ")
    print()
    print()
    while not stack == []:
        postfix.append(stack.pop(0))
    proses_stack(temp_stack, len_stack, postfix)

    
def main():
    while True:
        infix = input("Input Infix: ")
        print()
        infix_to_postfix(infix)
        print()
        coba = input("Press any key for exit program. Press y for repeat program ")
        print()
        if coba == 'y' or coba == 'Y':
            continue
        else:
            break
            
main()
