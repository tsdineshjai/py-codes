

# function to read inputs and put them into alist and return it 

def read_inputs_into_list() :
    list = [];

    i = 0
    while i < 5 :
        input_value = int(input("enter the number: "))
        list.append(input_value)
        i += 1
    return list

print(read_inputs_into_list())
# [1, 2, 3, 4, 5]