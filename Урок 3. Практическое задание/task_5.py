"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна
    выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова
    нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если
    вместо числа вводится специальный символ, выполнение программы завершается. Если специальный
    символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
    ранее сумме и после этого завершить программу.
"""
def summ_num():
    a=0
    while True:
        err= False
        in_list = input("Enter a number, input 'g' to exit:").split()


        for numm in in_list:
            if numm.lower()=="g":
                return a
            else:
                try:
                  a+= int(numm)
                except ValueError:
                    err = True

        if err:
         print("Data incorrect")
        print((f"summ of numbers={a}"))

summ_num()
