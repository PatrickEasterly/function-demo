# cats_name = "Oakley"
# print(f"Hayyyy {cats_name.upper()}")

cats = ['Oakley', 'Milla']

def greet(cat):
    print(f'Hello, {cat.upper()}')

for cat in cats:
    greet(cat)
greet('pat')
# greet() throws error, needs an argument
greet('')