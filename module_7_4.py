print('В команде Мастера кода участников: %(team1_num)s' % {'team1_num':'5'})
print('Итого сегодня в командах участников: %(team1_num)s, %(team2_num)s' % {'team1_num':'5', 'team2_num':'6'})
print('Команда Волшебники данных решила задач: {score_2}'.format(score_2 = '42'))
print('Волшебники данных решили задачи за {team1_time} c!'.format(team1_time = '18015.2'))



score_1 = 40
score_2=42
team1_num = 6 
team2_num = 6
team1_time = 1552.512 
team2_time = 2153.31451 
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'
print(f'Команды решили {score_1} и {score_2} задач')
print(f'Результат битвы: победа команды Мастера кода!')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.')

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'
