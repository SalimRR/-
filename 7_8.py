  
import random
def igra():
    igrok1 = random.randint(1, 6)
    igrok2 = random.randint(1, 6)
    if igrok1>igrok2:
        print('Победил игрок 1,', igrok1)
    elif igrok2>igrok1:
        print('Победил игрок 2,', igrok2)
    elif igrok1 == igrok2:
        print('Ничья')
igra()
