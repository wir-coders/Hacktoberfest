"""

Conversion of infix to postfix and it's evaluation

"""

def is_operand(ch):
    if ch.isalnum():
        return True
    return False

def priority(operator):
    dct = {'(':0,')':0, '+':1 , '-':1,'*':2,'/':2,'^':3}
    return dct[operator]

def in_to_post(s):
    stack = [ ]
    top = -1
    ops =[ ]
    for i in s:
        if is_operand(i):
            ops.append(i)
        elif i =='(':
            stack.append(i)
            top =top +1
        else:
            if stack:
                while top>-1 and (priority(stack[top])>=priority(i)):
                    tops=stack.pop()
                    top = top -1
                    if tops != '(':
                        ops.append(tops)
                    else :
                        break
                if i!=')':
                    stack.append(i)
                    top = top+1
            else:
                stack.append(i)
                top+=1
    if stack:
        for i in range(top+1):
            ops.append(stack.pop())
            top = top -1

    return ops



def solve(num1,num2,op):
	num1=float(num1)
	num2=float(num2)
	dct = {
		"+":num1+num2,
		"-":num1-num2,
		"*":num1*num2,
		"/":num1/num2
	}
	return dct[op]

def eval_post(lst):
	post=in_to_post(lst)
	stack = []
	top = -1
	for i in post:
		#print(stack)
		if i.isalnum():
			stack.append(i)
		else:
			num2=stack.pop()
			top-=1
			num1=stack.pop()
			top-=1
			stack.append( solve(num1,num2,i) )
			top+=1
	return stack[0]
			
if __name__ == "__main__":
    string = input("Enter infix(space seperated):").split()

    print("Postfix = "," ".join(in_to_post(string)))
    print("ans=",eval_post(string))

