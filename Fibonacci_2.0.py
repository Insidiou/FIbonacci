prev = 0
back = 0
current = 1
seq = int(input("How many digits of the Fibonacci Sequence do you want? "))
if seq < 1:
 print("no comprehendo")
elif seq == 1:
 print(0)
elif seq == 2:
 print(0)
 print(1)
elif seq == 3:
 print(0)
 print(1)
 print("2")
elif seq >= 4:
 print(0)
 print(1)
 seq = seq - 2
 while seq != 0:
  print(current + prev)
  back = prev
  prev = current
  current = current + back
  seq = seq - 1
