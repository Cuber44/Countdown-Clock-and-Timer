import time

def userinput():
    inputTime = input("Enter time in HH:MM:SS format only:\n")
    try:
        hourStr,minStr,secStr=inputTime.split(":")
        hours = int(hourStr)
        minutes = int(minStr)
        seconds = int(secStr)
        timeLeft = hours*3600 + minutes*60 + seconds
    except ValueError:
        print("Invalid time format. Please use HH:MM:SS.")
        userinput()
    finally:
        print("~"*100)
        return timeLeft
        


def countdownClock():
    myTime = userinput()
    for x in range(myTime,0,-1):
        second = x % 60
        minutes = (x//60)%60
        hours = x//3600
        print(f"{hours:02}:{minutes:02}:{second:02}")
        time.sleep(1)
    print("Time's Up!!")

    pass

def timer():
    myTime = userinput()
    for x in range(0,myTime):
        second = x % 60
        minutes = (x//60)%60
        hours = x//3600
        time.sleep(1)
        print(f"{hours:02}:{minutes:02}:{second:02}")
    print("Time's Up!!")

def main():
    while True:
        print("""1.Countdown Clock
2.Timer
3.Exit""")
        selection = int(input("Enter the option number: "))
        if selection == 1:
            countdownClock()
        elif selection == 2:
            timer()
        elif selection == 3:
            print("Exiting")
            break
        print("~"*100)

if __name__ == "__main__":
    main()