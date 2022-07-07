a=int(raw_input())

l=[ ]

while True:

      try:

           line = raw_input("")

      except EOFError:

           break

      l.append(line)

str=max(l,key=len)

print(len(str))
