

from concurrent import futures

def display(num):
    return num

if __name__=="__main__":
  lists = [z for z in range(1,100)]
  with futures.ThreadPoolExecutor(max_workers=5) as f:
      execute = [f.submit(display,num) for num in lists]
      for see in execute:
          print(see.result())


