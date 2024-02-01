#Dictionaries:

#1. Write a Python function to merge two dictionaries.

def merge_dicts(dict1,dict2):
    merge_dicts = dict1.copy()
    merge_dicts.update(dict2)
    return merge_dicts

dict1 = {'a' : 1, 'b' : 2}
dict2 = {'b' : 3, 'c' : 4}

result = merge_dicts(dict1, dict2)
print ("Merged Dictionary:", result)


# 2. Write a Python function to sort a dictionary by its values.

def sort_dict_by_values(input_dict):
    sorted_dict = dict(sorted(input_dict.items(),key = lambda item : item[1]))
    return sorted_dict

my_dict = {'a': 5, 'b':2, 'c': 8 ,'d' :1}

sorted_result = sort_dict_by_values(my_dict)
print("Original Dictionary:", my_dict)
print("Sorted Dictionary by Values:", sorted_result)