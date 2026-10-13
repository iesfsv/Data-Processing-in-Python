def sayHi(numberOfI: int = 1):

    if numberOfI > 10000:
        print("That would be too many 'i's, but Hi nonetheless")
        return

    print("H" + "i" * numberOfI)


def main():
    sayHi(1000000)


if __name__ == "__main__":
    main()
