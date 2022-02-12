import time as t

def bot():
    print("Starting bot ...")
    for i in reversed(range(3)):
        t.sleep(0.5)
        print(f"{i+1}")
    print("Say hi!")
    you = input()
    if you.lower() in ["hi", "greetings", "good day", "good afternoon", "good evening", "good morning"]:
        print(f"Bot: You are speaking English? Then {you}")
if __name__ == "__main__":
    bot()