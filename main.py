names = ['Кбубудущее', 'Ктиффлор', 'Ведророл', 'Гарпирия']
 
while True:
    name = input('Кто ты?\n-> ')
    if name not in names:
        print('Тут вообще ничего нет. Еще есть вопросы?')
    else:        
        print(f'Ты –свой. Приветствую, {name}! Пароль: 123456')
        break