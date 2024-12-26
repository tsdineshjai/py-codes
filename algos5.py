
#  a program to count the number of times an element is expressed in the list. 

list = [1,1,1,1,2,2,2,3,3,3]

def count_times_item(mylist) -> dict :

      dict = {}

      for ele in list :
        num_as_str = str(ele)
        if num_as_str in dict:
            dict[num_as_str] += 1
        else:
            dict[num_as_str] = 1
      return dict

print(count_times_item(list))


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