import time

def countdown( current,signal) :
    signals = [1, 2, 3, 4]
    countdowns=5
    if current == 1:
        while current == 1:
            print(f"Signal{signal} : Time Left : -")

    while current == 0:

        for signal in signals:
            for rem_time in range(countdowns,-1,-1):
                print(f"Signal {signal} : Time Left = {rem_time}")
                time.sleep(1)
        print("time's up")



