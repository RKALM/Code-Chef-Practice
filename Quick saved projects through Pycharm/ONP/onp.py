for _ in range(int(input())):
    s = input()
    stack = []
    output = ''

    for i in s:
        if i == '(' or i == '+' or i == '-' or i == '*' or i == '/' or i == '^':
            stack.append(i)
        elif i == ')':
            output += stack.pop()
            stack.pop()
        else:
            output += i
    print(output)