def reverse_string(input_string, word_bank):
    reversed = input_string[::-1]
    word_bank.append(reversed)

def find_unique(word_bank):
    uniques = []

    for chars in zip(*word_bank):
        if all(char == chars[0] for char in chars):
            uniques.append(chars[0])

    return ''.join(uniques)

word_bank = []
while True:
    input_string = str(input("Enter string to reverse (enter to print results): "))
    if len(input_string) == 0:
       break

    reverse_string(input_string,word_bank)

print("The strings reverse are:")
for item in word_bank:
    print(item)

print("\nThe unique string from all of them is: ")
print(find_unique(word_bank))
