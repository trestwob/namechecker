from namechecker import *

def main():
    print("Personality reveal of your name.\nPlease type your first name -> ", end=' ')
    name = input().strip().lower().replace(" ", '')
    obj = Namechecker(name)
    obj.printSpecs()

if __name__ == "__main__":
    main()
