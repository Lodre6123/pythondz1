"""Петя, Катя и Сережа делают из бумаги журавликов. 
Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, 
что Петя и Сережа сделали одинаковое количество журавликов, 
а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?"""
S = int(input("Введите четное число: "))
if S%2!=0:
    print("Вы ввели не четное число!")
else:
    K = int(S/3*2)
    P = int((S-K)/2)
    C = int(P)
    print("{} - {} - {}".format(K,P,C))