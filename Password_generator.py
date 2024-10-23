import random

#Characetrs that could be used for generating password
alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','*','+']

#Taking input to know how many alphabets, numbers and symbols will be used
alphabet_len = int(input('How many alphabets do you want to use in your password?\n'))
number_len = int(input('How many numbers do you want to use in your password?\n'))
symbol_len = int(input('How many symbols do you want to use in your password?\n'))

collection_of_elements = []

#Taking random alphabets, numbers and symbols as per given number of elements for each without repetition of elements 
collection_of_elements += random.sample(alphabets,alphabet_len)
collection_of_elements += random.sample(numbers,number_len)
collection_of_elements += random.sample(symbols,symbol_len)

#Shuffling the elements
random.shuffle(collection_of_elements)

#Creating string using the elments of list
password = ''.join(collection_of_elements)

print('Generated password :',password)
    

