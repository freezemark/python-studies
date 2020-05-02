problem = input('Введите задачу или "q" чтобы выйти: ')

while(problem != 'q'):
    print('Ответ на', problem, '- это', eval(problem))
    problem = input('Введите еще одну задачу или "q" чтобы выйти: ')