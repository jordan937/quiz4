from moduleA import function1 as modA
from moduleB import function2 as modB
from moduleC import function3 as modC

def main():
    modA.test()
    input = modB.getValue()
    print(f"From modB I got the value {input}")
    input = modC.adding(input)
    print(f"Using modC I changed input's value to {input}")

if __name__=="__main__":
    main()