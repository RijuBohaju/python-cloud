my_list=[1, 2, 3, 4, 5]
a = my_list
b= [2, 4, 6]
is_same_object = a is my_list
is_not_same_object = b is not my_list

element_in_list = 2 in my_list
element_not_in_list= 6 not in my_list

print("a is my_list:", is_same_object)
print("b is not my_list:", is_not_same_object)
print("3 includes:",element_in_list)
print("6 not in list:", element_not_in_list)