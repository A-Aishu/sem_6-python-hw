def Merge_Dictionaries(first, second):
    result = {**first_Dict, **second_Dict}
    return result

first_Dict = {'a': 'apple', 'b': 'Banana' , 'o': 'Orange'}
second_Dict = { 'k': 'Kiwi', 'm': 'Mango'}
print("First Dictionary: ", first_Dict)
print("Second Dictionary: ", second_Dict)

third_Dict = Merge_Dictionaries(first_Dict, second_Dict)

print("\nAfter merging two Dictionaries : ")
print(third_Dict)
