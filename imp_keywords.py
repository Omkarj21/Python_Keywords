print(5 > 3)  # True
print(3 > 7)  # False

# None
print(None == 0) # False
print(None == []) # False
x = None
y = None
print(x == y) # False
# --------------------------------
# assert
a = 8
assert a < 15, "Correct"
assert a > 15, "Incorrect"
# --------------------------------
for i in range(1,5):
    if i == 2:
        break
    print(i)
# --------------------------------
for i in range(1,5):
    if i == 3:
        continue
    print(i)
# ------------------------------
def outer_function():
    a = 5
    def inner_function():
        nonlocal a
        a = 10
        print("Inner function: ",a)
    inner_function()
    print("Outer function: ",a)
outer_function()
# ------------------------------