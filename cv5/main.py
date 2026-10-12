def test_fun():
    i = 5
    j = 10
    return i, j

lst = [1, "Ahoj", None] # List
print (f"lst[0] -> {lst[0]}") 
print (len(list))
for item in lst:
    print(item)

if 1 in lst:
    pass
lst[-1] = 5
i, j = test_fun()

tpl = (1, 2, 3) # Tuple
print (f"tpl[0] -> {tpl[0]}")
print (len(tpl))
for item in tpl:
    print(item)

st = {1,2,1,3,1,2,1} # Set
print (f"st[0] -> {st[0]}")
print (len(st))
for item in st:
    print(item)

dct = {
    "key": "value",
    1       :   5
}
print(dct{"key"})