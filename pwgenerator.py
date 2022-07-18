import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Brennan's Password Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
rletters = []
rnumbers = []
rsymbols = []
for x in range(0, nr_letters):
  randlet = letters[random.randint(0,len(letters)-1)]
  rletters.append(randlet)
for y in range(0, nr_numbers):
  randnum = numbers[random.randint(0,len(numbers)-1)]
  rnumbers.append(randnum)
for z in range(0, nr_symbols):
  randsymb = symbols[random.randint(0,len(symbols)-1)]
  rsymbols.append(randsymb)

pwgen =  rletters + rnumbers + rsymbols

scrgen = random.shuffle(pwgen)

pwgenerator = "".join(pwgen)

print(f"Here is your randomly generated password: {pwgenerator}")