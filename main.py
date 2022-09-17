from math_function import tambah,kali,bagi


def main():

    data_1 = int(input("masukkan input 1 :"))
    data_2 = int(input("masukkan input 2 :"))
    operator = input("masukkan operator :")

    if operator == "+":
        result = tambah(data_1, data_2)
    elif operator == "*":
        result = kali(data_1, data_2)
    elif operator == "/":
        result = bagi(data_1, data_2)
    else :
        print("ERROR")

    print("{} {} {} = {} ".format(data_1, operator, data_2, result))


if __name__ == "__main__":
    print("Hello Main !")
    main()