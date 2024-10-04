print(bool(None))
def simple_generator():
    yield 1
    yield 2
    yield 3

# Using the generator
gen = simple_generator()
# Iterate through the generator
for value in gen:
    input()
    print(value)
