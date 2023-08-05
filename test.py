def fibonacci(n):
  """ summary

  Args:
    n (int): the first parameter

  Returns:
    int: an integer for which each term is the sum of the two preceding terms.

  """
  
  # first case
  
  if n<=1:
      
    return n

  # recursive case
  
  else:
      
    return fibonacci(n-1) + fibonacci(n-2)





n = int( input("Entrez le nombre de termes:"))


print("Suite de Fibonnaci en utilisant la recursion :")


# output 


for i in range(n):
  
  print(fibonacci(i))
