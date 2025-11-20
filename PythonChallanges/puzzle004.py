## given string = "KiranKumar2025"
## expecrted output = "KIRANKUMAR"
str = "KiranKumar2025"
result = [char.upper() for char in str if char.isalpha()]
print(result)
result = ''.join(result)
print(result)