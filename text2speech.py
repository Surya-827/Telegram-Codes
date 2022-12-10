import pyttsx3 as p

def male(msg,rate,volume):
    #Rate > 200, volume limit 0-1
    converter = p.init()
    converter.setProperty('rate', rate)
    converter.setProperty('volume', volume)
    converter.say(msg)
    converter.runAndWait()

def defaultSpeak(text):
    engine = p.init()
    engine.say(text)
    engine.runAndWait()

def enterText():
    print("Enter Your Text Here | ")
    defaultSpeak("Enter Your Text Here")
    text = input()
    if text.lower()!="bye":
        return enterText()
    defaultSpeak(text + "?")
    return text

if __name__=="__main__":

    reply = enterText()
    msg_count = 0

    while reply!="bye":
        reply
    else:
        male("Bye Bye Catch you later!", 160, 1)

