age = int(input("Talk true how old you d? "))
if age >= 18:
  print("You are an adult")
else:
#   print("You d small")
password = input("Type the rubbish wey d ur mind as password: ")
if password == "Gerald":
	print("For your mind you remember your password")
else:
	print("😂😂😂🤣🤣 you no remember am🤣🤣")
num = int(input("werey type one rubbish: "))
if num > 0:
  print("Positive")
elif num < 0:
  print("Negative")
else:
  print("Zero")

score = int(input("What's your score? "))
if score >= 70:
  print("A")
elif score >= 60:
  print("B")
elif score >= 50:
  print("C")
elif score >= 45:
  print("D")
else:
  print("F")

name = input("Enter your full name: ")
age = int(input("How old are you: "))
if age >= 18:
  print(name, "you are eligible to vote.")
else:
  print(name, "you are NOT eligible to vote.")
  
num = int(input("Enter a number: "))
if num % 2 == 0:
  print("The number is Even")
else:
  print("The number is Odd")

print("Welcome to Gerald's Bank😁")
pin = int(input("Enter your 4-digit pin: "))
balance = 10000 
if pin == 1234:
  print("Login Successful")
  print("\n MENU")
  print("1. Check Balance")
  print("2. Withdraw Money")
  print("3. Deposit Money")
  print("4. Exit")
  
  choose = int(input("\nEnter your choice (1-4) "))
  if choose == 1:
    print(f"Your balance is #10000")
  elif choose == 2:
    amount = int(input("Enter amount to withdraw: "))
    if amount <= balance:
      print(f"Insufficient funds")
    if amount >= balance:
      print(f"Withdrawal successful")
  elif choose == 3:
    amount = int(input("Enter amount to deposit: "))
    balance += amount
    print(f"Deposit successful! New balance: #{balance}")
  else:
    print("Invalid Option!")
else:
    print("Incorrect Pin")





print("=== Student Admission Checker ===")
score = int(input("Enter JAMB Score: "))
department = input("Enter Department: ")
department = department.lower()
if department == "medicine":
  cutoff = 350
  if score >= cutoff:
    print("Congratulations, you are admitted into Medicine!")
  else:
    print("Sorry, you were not admitted.😔")
    print("Try again next year")
elif department == "engineering":
  cutoff = 250
  if score >= cutoff:
    print("Congratulations, you are admitted into Engineering!")
  else:
    print("Sorry, you were not admitted.")
    print("Try again next year")
elif department == "law":
  cutoff = 240
  if score >= cutoff:
    print("Congratulations, you are admitted into Law!")
  else:
    print("Sorry, you were not admitted.😔")
    print("Try again next year")
elif department == "business":
  cutoff = 180
  if score >= cutoff:
    print("Congratulations, you are admitted into Business!")
  else:
    print("Sorry, you were not admitted.")
    print("Try again next year")
else:
    print("Invalid Department! Try Medicine, Engineering, Law, or Business.")





    
    
