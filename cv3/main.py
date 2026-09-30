# aritmicke op.

## and or
# prirazovaci
## =, +=, -=, *=, /=
# bitovy
## &, |, ^, <<, >>, ~

# A = 0b10100111
# B = 0b10011010
 
# A & B = 0b10000010
# A | B = 0b10111111
# A ^ B = 0b00111101
# ~A = 0b01011000
# A << 4 = 0b01110000
# B >> 4 = 0b00001001

## Nactete INT ze vstupu a naformatujte ho na hh:mm:ss

## 360 -> 00:06:00
def time ():
    if __name__ == "__main__":
        str_time = input("Zadej cas v s: ")
        time = int(str_time)
        hour = time // 3600
        minut = (time % 3600) // 60
        second = (time % 3600) % 60
        print(f"{hour}:{minut}:{second}")

if __name__ == "__main__":

    def money():
        str_money = input("Zadej pocet penez: ")
        value = int(str_money)
        x_5000 = value // 5000
        value = value - (x_5000 * 5000)
        x_2000 = value // 2000
        value = value - (x_2000 * 2000)
        x_1000 = value // 1000
        value = value - (x_1000 * 1000)
        x_500 = value // 500
        value - value - (x_500 * 500)
        x_200 = value // 200
        value - value - (x_200 * 200)
        x_100 = value // 100
        value - value - (x_100 * 100)
        x_50 = value // 50
        value - value - (x_50 * 50)
        x_20 = value // 20
        value - value - (x_20 * 20)
        x_10 = value // 10
        value - value - (x_10 * 10)
        x_5 = value // 5
        value - value - (x_10 * 10)
        x_2 = value // 2 
        value - value - (x_10 * 10)
        x_1 = value // 1
       

    money()


    ## pt = value // 5000
           ## dt = (value % 5000) // 2000
           ## jt = ((value % 5000) % 2000) // 1000
           ## ps = (((value % 5000) % 2000) % 1000) // 500
           ## ds = ((((value % 5000) % 2000) % 1000) % 500) // 200
           ## js = (((((value % 5000) % 2000) % 1000) % 500) % 200) // 100
           ## pak = ((((((value % 5000) % 2000) % 1000) % 500) % 200) % 100) // 50
           ## dvk = (((((((value % 5000) % 2000) % 1000) % 500) % 200) % 100) % 50) // 20
           ## dek = ((((((((value % 5000) % 2000) % 1000) % 500) % 200) % 100) % 50) % 20) // 10
           ## pk = (((((((((value % 5000) % 2000) % 1000) % 500) % 200) % 100) % 50) % 20) % 10) // 5
           ## dk = ((((((((((value % 5000) % 2000) % 1000) % 500) % 200) % 100) % 50) % 20) % 10) % 5) // 2
           ## jk = ((((((((((value % 5000) % 2000) % 1000) % 500) % 200) % 100) % 50) % 20) % 10) % 5) % 2
           ## print(f"5000* {pt}, 2000: {dt}, 1000: {jt}, 500: {ps}, 200: {ds}, 100: {js}, 50: {pak}, 20: {dvk}, 10: {dek}, 5: {pk}, 2: {dk}, 1: {jk}")