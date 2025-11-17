import time

number = 0
while number <= 20:
  time.sleep(1)
  print(number)
  number += 1
  
  
  
while True:  
  password = input("Enter your password: ").lower()
  if password == "admin":
    time.sleep(3)
    print("Correct Password")
    break
  elif password != "admin":
    time.sleep(2)
    print("Incoorect Password")
      

number = 2
while number <= 10:
  time.sleep(3)
  print(number)
  number += 2



while True:
  number = int((input("Enter a number: ")))
  if number > 0:
    print("positive")
  elif number < 0:
    print("negative")
  else:
    print("Zero")
  exit = input("Press exit if you want to quit: ").lower()
  if exit == "exit":
    print("Goodbye!")
    break
  elif exit == "no":
    continue
    
      
      

      
