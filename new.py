#1
def add(num1,num2):
  sum = num1+num2
  return(sum)

Fnum = int (input("enter first number:"))
Snum = int (input("enter second number:"))
sum = add(Fnum,Snum)
print(f"sum is{sum}")



Brand_name = input ("Enter brand name")
Model_name =("Enter model name")
price = int(input("enter price"))

def Laptop_specs(brand,model,price):
     print (f"the laptop id{brand}, {model} @ Rs.{price}")

mylaptop=Laptop_specs(Brand_name, Model_name, price)
print(myLaptop)




#working model of atm machine
total_price = 0
card_type = "visa"
is_same_bank = True
is_expired =False

print("please insert your atm card:")
required_amt =int(input("please enter a amount:"))

def read_card():
    card_details = [1200,False,False]
    total_price = card_details[0]
    is_same_bank=card_details[1]
    is_expired=card_details[2]
    if is_expired: 
        print("Sorry,this card can not be accepted here")
    else:
        peform_transaction(total_price,is_same_bank)



    def perform_tansaction(total_amt, is_same_bank):
    charge = 0
    if not is_same_bank:
        charge = 5
        if required_amt > total_amt:
            return "Not enough balance"
        else:
            print(f"Ant withdrwn: {required_amt}")
            print(f"Remaining available balance: {total_amt-required_amt-charge}")
    else:
        if required_amt > total_amt:
            return "Not enough balance"
        else:
            print(f"Ant withdrwn: {required_amt}")
            print(f"Remaining available balance: {total_amt-required_amt-charge}")


