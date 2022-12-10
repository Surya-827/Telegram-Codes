
import pyautogui as p
import time as t
import random as r

def messageShuffler(st) -> str:
    newMsg = ""
    temp = r.shuffle(list(str).split(" "))
    for i in temp:
        newMsg+=i
    return newMsg

t.sleep(4)
# limit = int(input("Enter Message Limit : "))
# msg = input("Please Leave a message here : ")
count =0
limit=100
msg = ["oorike","sarada","bored","Hi","miss you","any plans?","happy weekend"]

k = r.randint(0,len(msg))

while count<=limit:
    # p.typewrite("I am Sorry ! "+str(count))
    r.shuffle(msg)
    p.press("enter")
    r.shuffle(msg)
    count+=1
print(f"{limit} Messages Sent Succesfully !")

# import pyautogui as p
# import time as t
# import random as r
#
# class WhatsappAutoMsg:
#     def autoSendMessages(msg,limit):
#         count=0
#         while count<=limit:
#             p.typewrite(msg)
#             p.press("enter")
#             count+=1
#         print(f"Your {limit} Messages Sent Successfully!")
#
# if __name__=="__main__":
#
#     obj = WhatsappAutoMsg()
#     my_message = "Hi ra!"
#     limit=10
#     obj.autoSendMessages(my_message,limit)

