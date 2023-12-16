
f = open("input", "r")
l = [  n.replace("\n","" ) for n in f.readlines()  ]


'''
The HASH algorithm is a way to turn any string of characters into a single number in the range 0 to 255. To run the HASH algorithm on a string, start with a current value of 0. Then, for each character in the string starting from the beginning:

    Determine the ASCII code for the current character of the string.
    Increase the current value by the ASCII code you just determined.
    Set the current value to itself multiplied by 17.
    Set the current value to the remainder of dividing itself by 256.
'''


print(l)
instruction = l[0].split(",")


def has(current_char):
    global current_value 
    current_value += ord(current_char)
    current_value *= 17
    current_value = current_value % 256
    return current_value

tot = 0
for string in instruction:
    current_value = 0
    for char in string:
        has(char)
    print(string, current_value)
    tot += current_value
    
print(tot)