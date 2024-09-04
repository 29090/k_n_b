import random

while True:

    user= int(input("Введите число: \n1-Камень \n2-Ножницы\n3-Бумага\n"))
    computer=random.randrange(1,4)

    a=user-computer
    if a==0:
        print("У Вас ничья! Попробуйте еще!")
    elif a==-1 or a==2:
        print("Пользователь победил!")
    else:
        print("Машина победила!")
    print(computer)


    # if user==computer:
    #     print("У Вас ничья! Попробуйте еще!")
    # elif (user==1 and computer==2) or \
    #     (user==2 and computer==3) or (user==3 and computer==1):
    #     print("Пользователь победил!")
    # else:
    #     print("Машина победила!")
