# Conditional operators:

is_raining = False
is_cold = False
print("Good Morning")
# anything under indendation of `if` will consider
# as body of `if`, same for `elif` and `else`.
if is_raining and is_cold:
    print("Bring Umbrella and jacket")
elif is_raining and not(is_cold):
    print("Bring Umbrella")
elif not(is_raining) and is_cold:
    print("Bring Jacket")
else:
    print("Shirt is fine!")