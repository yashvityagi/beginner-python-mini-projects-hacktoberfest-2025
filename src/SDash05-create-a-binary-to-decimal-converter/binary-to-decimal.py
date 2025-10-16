
def func():
  binary = input("Enter the binary value here:\n") 
  for x in binary:
    if x!='0' and x!='1':
      print("Invalid value")
      break
      
  decimal = int(binary,2)
  print("The value in form of decimal is : ",str(decimal))

func()
