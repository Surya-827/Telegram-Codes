
import math as m

def Solution(amount):
    notes = []
    if(amount!=0):
        note2k = (amount/2000)
        note5h = ((amount-(note2k*2000))/500)
        note1h = ((amount-(note2k*2000) + (note5h*500))/100)

        notes.append(note2k)
        notes.append(note5h)
        notes.append(note1h)
    return notes


amount=700
print(Solution(amount))