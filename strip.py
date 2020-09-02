

slayers = "Buffy and Faith999"

print(slayers.strip("999"))


string="AbCdEf"

print(string.swapcase())

string="kumar"
print(string.capitalize())

string="SINGH"
print(string.lower())

string="pawan"
print(string.upper())

string=" abcdefghijklmnop"
print(string.find("i"))

print(string.find("z"))

print(string.find("op"))


print(string.index("p"))

#if not found then throws ValueError this is the main difference between find() vs index() methods

#print(string.index("z"))


''' count(string,start,end) '''
string = "apple is apple and only apple"

print("count =",string.count("apple",0,-1))

print("count =",string.count("apple"))
