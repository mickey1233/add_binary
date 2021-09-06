def addbinary(a, b):
    # return bin(int(a,2) + int(b,2))[2:]
    print(bin(int(a, 2) + int(b, 2)).replace("0b", ""))


def main():
    addbinary("11", "1")
    addbinary("1010", "1011")


if __name__ == "__main__":
    main()
