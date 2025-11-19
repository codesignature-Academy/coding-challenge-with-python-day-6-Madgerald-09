import time
try:
  start_time = int(time.time())
  print("<==========>SQUARE NUMBERS CALCULATOR<==========>")
  N = int(input("Enter a number: "))
  squares = []
  for i in range(1, N + 1):
    # squares.append(i * i)
    squares.append(i ** 2)
    time.sleep(2)
  print("Squares of numbers from 1 to", N, "are: ", squares)
except ValueError:
  print("Number must be in digits !!")
end_time = int(time.time())  
execution_time = end_time - start_time 
print(f"Execution time = {execution_time} seconds")
