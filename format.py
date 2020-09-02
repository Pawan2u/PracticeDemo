"""

print("{0} {1}".format("I'm David","I'm best"))


print("My name is {name} and I man {age} years old".format(name="_David",age=17))

print("{} {} {}".format("Hello","Python","Lovers"))


"""


hero="David"

number=50

print("Element {number} is a {hero}".format(**locals()))



slayers="Buffy\nFaith"

print(slayers.splitlines())

slayers="Buffy*Slaying-Vamps*16"

fields=slayers.split("*")

print(fields)

job=fields[1].split("-")

print(job)