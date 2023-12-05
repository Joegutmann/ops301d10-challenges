import os

def ch5():
    t1 = "whoami"
    t2 = "ip a"
    t3 = "lshw -short"

    print(t1)
    print(t2)
    print(t3)

    os.system("whoami")

    os.system("ip a")

    os.system("lshw -short")

if __name__ : "__main__"
ch5()

# it pushed an empty folder so I just cnp'd it here directly.
