sp = set()
art = set()
all_st = set(chr(i) for i in range (ord('A'), ord('Z') + 1)) 
for i in all_st:
    if input(f'Студент {i} заниммется спортом?\nY - yes; N - No\n') == 'N':
        art.add(i)
    else:
        sp.add(i)
        art.add(i) if input(f'Студент {i} заниммется Искусством?\nY - yes; N - No\n') == 'Y' else None
sp_and_art = sp&art
print(f'''
Только спортом занимаются студенты {sp}
Только искусством занимаются студенты {art}
Искусством и спортом занимаются студенты {sp_and_art}''')
print(len(sp), len(art), len(sp_and_art), len(sp.union(art)))