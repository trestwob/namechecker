from namechecker.namechecker import Namechecker

def main():
    name = input("Please type your name -> ").strip().lower()
    obj = Namechecker(name)
    obj.printSpecs()

if __name__ == "__main__":
    main()
