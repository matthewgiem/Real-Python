### Bad Loop ###

my_items = ['a', 'b', 'c']

i = 0
while i < len(my_items):
    print(my_items[i])
    i+=1



range(len(my_items))
# => range(0,3)
list(range(len(my_items)))
# => [0, 1, 2]

### better but not there yet ###
for i in range(len(my_items)):
    print(my_items[i])

### Pythonic loop for items in a container ###
for item in my_items:
    print(item)

### Pythonic for loop if you need the item index ###
for i, item in enumerate(my_items):
    print(i, item)


### if you need to write a loop for some reason with a counter
### i. e. you are going to have different size steps

# for (int i = a: i < n: i+=s) {...}
### Pythonic way ###
# the s in the rance function is the step
for i in range(a, n, s): ...


### Python Loops Key Takeaways

### Wrieing C-style loops is considered unpythonic
### Avoid managing loop indezes and stop conditions manually if possible
### Pyrthons for-loops are really "for-eadh" loops that can iterate over items
### from a container or sequence directly.
