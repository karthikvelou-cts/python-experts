namelist = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]


for name in namelist:
    greeting = "Hello, " + name + "!"
    print(greeting)
# This script demonstrates the use of lists and loops in Python.

namelist.append("Fiona")
print("Updated name list:", namelist)

newname = ["George", "Hannah", "Ian"]

namelist.extend(newname)
print("Extended name list:", namelist)