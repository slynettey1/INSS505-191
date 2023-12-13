def is_prime(n):
  # 0 and 1 are not prime
  if n < 2:
    print("false")
  # 2 is the only even prime
  if n == 2:
    print("True")
    # All other even numbers are not prime
  if n % 2 == 0:
    print("False")
  # Check odd divisors from 3 to sqrt(n)
  for i in range(3, int(n**0.5) + 1, 2):
    if n % i == 0:
      print("False")
  # If no divisor is found, the number is prime
  print("True")

# A loop to ask the user for a positive number
while True:
  # Ask the user to enter a number
  num = int(input("Enter a number > 0: "))
  # If the number is positive, break the loop
  if num > 0:
    break
  # Otherwise, print an error message and repeat the loop
  else:
    print("Wrong input. Please enter a number > 0.")

# Check if the number is even or odd
if num % 2 == 0:
  print(num, "is an even number.")
else:
  print(num, "is an odd number.")

# To check if the number is prime or nonprime
if is_prime(num):
  print(num, "is a prime number.")
else:
  print(num, "is a nonprime number.")
