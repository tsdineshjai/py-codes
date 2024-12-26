
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