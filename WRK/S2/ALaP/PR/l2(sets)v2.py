sport = set(input('Введите имена учеников, которые увлекаются спортом, через запятую:').split(', '))
art = set(input('Введите имена учеников, которые увлекаются искусством, через запятую:').split(', '))
print(sport, art)

both = sport.intersection(art)
print(f'Ученки, которые интересуются и спортом, и искусством: {both}')

