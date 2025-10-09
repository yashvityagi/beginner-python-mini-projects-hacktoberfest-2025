while True:
    value=input("Enter binary value for conversion =").strip()
    if value=="":
        print("Error! input cannot be empty:Please try again =")
        continue
    if not all (digit in "01" for digit in value):
        print("Error only 0 and 1 are allowed")
        continue
    break


result = 0
power=0

for i in reversed(str(value)):
    result = result + (int(i) * 2**power)
    power+=1
    
print(result)
