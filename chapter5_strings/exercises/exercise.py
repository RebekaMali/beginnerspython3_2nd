my_string = "Danyse,Marie,Smyth,21,UK,London".replace(",", " ")
# print(my_string)

first_string = input("type first string ")

second_string = input("type second string ")

third_string = first_string + " " + second_string

print(third_string)

print(len(third_string))

upper_string = third_string.upper()
print(upper_string)

contains_string = third_string.__contains__("Pamela")
print(contains_string)