#create a function and calling of function

'''
syntax: 
#creating function 
def function_name():
    #you can do anything here
    return........something
    
#calling function 
function_name()

'''

#example:

#creating_function 
def duita_num_joda():....
    sum=3+5
    print (sum)
    return sum

#calling function with their name


# taking input from user:
# my_name=input ("please enter your name -->: ")
# print("ma sanga stored bhako value yei ho-->",my_name)


f_name = input("Enter first name")
s_name = input("Enter last name") 

def full_name_generator(first_name,second_name):
 full_name = first_name + second_name
  return full_name

print("your full name is;", full_name_generator(f_name,s_name))


