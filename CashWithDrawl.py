import math as m

def solution(amount):
  notes = [2000,500,200,100]
  count = [0]*len(notes)
  dp = list()
  for i in range(len(notes)):
    if(amount>=notes[i]):
      count[i] = m.floor(amount/notes[i])
      amount = amount - count[i] * notes[i]

  for j in range(len(notes)):
    if(count[j]!=0):
      dp.append(notes[j])
  return dp


if __name__=="__main__":
  amount=int(input())
  print(solution(700))