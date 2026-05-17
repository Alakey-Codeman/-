menu = ['1 — Добавить ученика', '2 — Посмотреть всех учеников', '3 — Показать лучшего ученика', '4 — Показать средний балл', '5 — Найти двоечников', '6 — Выход']
students = []
names = []
#Главное меню
while True:
        for options in menu:
            print(options)
        inp = input('Ваш запрос: ')
        if inp == '6':
            quit()
        elif inp == '1':
#add student
            while True:
                marks = []
                name = input('Введите имя ученика: ')
                if name in names:
                    print('not new')
                elif name == 'stop':
                    break

# add marks
                while True:
                    try:
                        mark = int(input('Введите оценку (или 11, чтобы завершить): '))
                        if mark <= 10:
                            marks.append(mark)
                            continue
                        else:
                            if name not in names:
                                try:
                                    sred = sum(marks)/len(marks)
                                    print('Добавлен ', name, 'Средняя оценка: ', sred , 'Все: ', marks)
                                    students.append([name, sred, marks])
                                    names.append(name)
                                    break
                                except ZeroDivisionError:
                                    print(name, 'Нет оценок')
                                    continue
                            else:
                                for student in students:
                                    if student[0] == name:
                                        student[2].extend(marks)
                                        try:
                                            sred = sum(student[2]) / len(student[2])
                                            student[1] = sred
                                        except ZeroDivisionError:
                                            print(name, 'Нет оценок')


                                        print('Оценки обновлены')
                            break

                    except ValueError:
                        print('Error, enter a number between 1 and 10 or greater to exit cycle')
                        continue
#everybody
        elif inp == '2':
            for student in students:
                print(student)
#school average
        elif inp == '4':
            common = 0
            st = 0
            for student in students:
                common += sum(student[2])
                st += len(student[2])

            average = common / st
            print(average)
#best dude
        elif inp == '3':
            try:
                best = max(students, key=lambda student: student[1])

                print(best)
            except IndexError:
                print('no students found')
#find two-markers
        elif inp == '5':
            print('Список двоечников: ')
            two = []
            for student in students:
                if student[1] < 3:
                    two.append(student)
            if two == []:
                print('Не найдены')
            else:
                for tw in two:
                    print(tw)




        else: print('Введите корректное значение')
        continue


