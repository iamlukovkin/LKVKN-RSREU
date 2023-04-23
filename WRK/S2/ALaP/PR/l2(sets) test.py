import random; import time
from progress.bar import IncrementalBar

bar = IncrementalBar('In progress', max = 10000)

k = 0
for j in range (10000):
    bar.next()
    sp = set()
    art = set()
    all_st = set(chr(i) for i in range (ord('A'), ord('Z') + 1)) 
    for i in all_st:
        s = 'Y' if random.randint(0,1) == 1 else 'N'
        #print(f'Студент {i} заниммется спортом?\nY - yes; N - No\n{s}')
        if s == 'N':
            art.add(i)
        else:
            sp.add(i)
            a = 'Y' if random.randint(0,1) == 1 else 'N'
            #print(f'Студент {i} заниммется Искусством?\nY - yes; N - No\n{a}')
            art.add(i) if a == 'Y' else None
    sp_and_art = sp&art
    #print(f'''
    #Только спортом занимаются студенты {sp}
    #Только искусством занимаются студенты {art}
    #Искусством и спортом занимаются студенты {sp_and_art}''')
    k += 1 if len(sp) > len(art) else 0
bar.finish()
print(f'{k/1000000*100}%')
