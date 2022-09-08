numbers = int(input("enter number:"))


def filter(ran):
    odd=[]
    even=[]
    for i in range(ran):
        if(i%2 == 0) and (i !=0):
            even.append(i)
        else:
            odd.append(i)
    print(f"even list is :{even},odd list is :{odd}")

filter(numbers)
 

        

