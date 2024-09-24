ans1 = input("Сейчас зима?\n")
ans1 = ans1.lower()
if ans1 == "да" or ans1 == "yes":
    ans2 = input("Идёт снег?\n")
    ans2 = ans2.lower()
    if ans2 == "да" or ans2 == "yes":
        print("Наденьте комбинезон или куртку. Не забудьте капюшон!")
    elif ans2 == "нет" or ans2 == "no":
        print("Наденьте комбинезон или куртку. Капюшон можете не недевать")
    else:
        print("Вы ввели что-то не то")
elif ans1 == "нет" or ans1 == "no":
    ans2 = input("Сейчас лето?\n")
    ans2 = ans2.lower()
    if ans2 == "да" or ans2 == "yes":
        ans3 = input("Идёт дождь?\n")
        ans3 = ans3.lower()
        if ans3 == "да" or ans3 == "yes":
            print("Надень шорты и майку, а сверху одноразовый дождевик или возьми зонт. Если хочешь прыгать по лужам, надень сапоги")
        elif ans3 == "нет" or ans3 == "no":
            print("Надень шорты и майку, а на голову кепку. Возьми с собой бутылку воды.")
        else:
            print("Вы ввели что-то не то")
    elif ans2 == "нет" or ans2 == "no":
        ans3 = input("Сейчас весна или осень?\n")
        ans3 = ans3.lower()
        if ans3 == "да" or ans3 == "yes":
            ans4 = input("Идёт дождь?\n")
            ans4 = ans4.lower()
            if ans4 == "да" or ans4 == "yes":
                print("Надень ветровку и тёплые штаны и возьми зонт.")
            elif ans4 == "нет" or ans4 == "no":
                print("Надень ветровку и тёплые штаны")
            else:
                print("Вы ввели что-то не то")
        elif ans3 == "нет" or ans3 == "no":
            print("Не могу понять")
        else:
            print("Вы ввели что-то не то")
    else:
        print("Вы ввели что-то не то")
else:
    print("Вы ввели что-то не то")