def who_are_you_and_hello():
    while True: 
        s = input().split()
        if len(s) == 1:
            if s[0].isalpha():
                if s[0][1:].islower():
                    if s[0][0].isupper():
                        print("Привет, " + " ".join(s) + "!")
                        break
