def triangular(n):
  if (n < 0):
    return print("Hanya Masukkan bilangan positif")
  elif (type(n) != int):
    return print("Hanya Masukkan bilangan bulat")

  return int(n * (n+1)/2)

print(triangular(5))
triangular(-5)
triangular(5.2)