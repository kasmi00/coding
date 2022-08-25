days_list =['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
#index_list =['1','2','3','4', '5', '6','7']
my_value = days_list[3]


print(my_value)

#append() method
#--> It is used to insert into the exisiting list
#print(days_list)
#days_list.append("kasmiday")
#print(days_list)

print("your recent days")

for day in days_list:
    print(day,end="")


#pop()
#-->It is used to eject the last element/item from the list and return to us.
print(days_list)
days_list.pop(2)
print(days_list)
