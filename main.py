from math import sqrt

#### Fonction secondaire


def isprime(p):
    for i in range(2,p):
        if p%i==0:
            return False
    return True

#### Fonction principale


def main():
    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()

if __name__ == "__main__":
    main()