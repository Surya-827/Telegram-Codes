import psutil as p
import time as t


def convertTime(seconds):
    min,sec = divmod(seconds,60)
    hours,min = divmod(min,60)
    return "%d:%02d:%02d" % (hours,min,sec)

battery = p.sensors_battery()
t.sleep(0.5)
print(f"Battery Percentage : {battery.percent}")
t.sleep(0.5)
print(f"Charger Plugged In : {battery.power_plugged}")
t.sleep(0.5)
print(f"Battery Left : {convertTime(battery.secsleft)}")



if __name__=="__main__":

    #check = Value
    if battery.percent < 20:
        speak("Please Plug in your Charger")
    elif battery.percent == 100:
        speak("Battery is Full Please Remove Your Charger")
    else:
        speak("Keep Coding battery backup is available")