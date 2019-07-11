 #print ("Welcome to my Calculator")

add1 = int(raw_input("Enter a number: "))
add2 = int(raw_input("Enter another number: "))

def myAddFunction(add1, add2):
     sum = add1 + add2
     return sum


print("Here is the sum: "+ str(myAddFunction(add1, add2)))


#sub


def mySubFunction(sub1, sub2):
    sub = sub1 - sub2
    return sub


print("Here is the difference: "+ str(mySubFunction(add1, add2)))


#mul

def myMulFunction(mul1, mul2):
    answer = mul1 * mul2
    return answer


print("Here is the product: "+ str(myMulFunction(add1, add2)))
