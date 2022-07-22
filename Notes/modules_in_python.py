# Modules: 
# https://docs.python.org/3/py-modindex.html : list of all modules in python.

# import multiple modules by comma separator.
# Now string only use as `st` not as `string`. 
import platform, string as st
import os

# import specific function from module
# from platfrom import python_version
# print(python_version()) #OP: 3.7.0

# get all methods inside the `platform` class.
print(dir(platform))

# Acces methods inside the modeule:
print(platform.python_version())    #OP: 3.7.0

# Shows ystem we are on:
print(platform.system())    #OP: Win32



