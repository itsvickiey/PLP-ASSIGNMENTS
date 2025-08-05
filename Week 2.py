# Empty list
my_list= []
# Appending elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)
#changing the second element
my_list[1] = 15
print(my_list)
# extending the list with another list
my_list.extend([50, 60, 70])
print(my_list)
#removing the last element
my_list.pop()
print(my_list)
#Sort the list in ascending order
my_list.sort()
print(my_list)
#printing the index of the element 30
print(my_list.index(30))
