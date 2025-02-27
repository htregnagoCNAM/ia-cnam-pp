def min_max(input_list):
    return min(input_list),max(input_list)

def squared_list(input_list):
    return [number ** 2 for number in input_list]

def is_palindrome(input_string):
    return input_string == input_string[::-1]

newList = [10, 4, 6, 3, 89, 45]
print(f"La liste initiale : {newList}")

sortedSquaredList = sorted(squared_list(newList))
print(f"La liste triée au carré : {sortedSquaredList}")

print(f"Le tuple min/max : {min_max(newList)}")

kayak = "KAYAK"
toto = "TOTO"
print("KAYAK est un palindrome" if is_palindrome(kayak) else "KAYAK n'est pas un palindrome")
print("TOTO est un palindrome" if is_palindrome(toto) else "TOTO n'est pas un palindrome")