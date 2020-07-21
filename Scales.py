# Major : T T ST T T T ST
# Minor : T ST T T ST T T
# Minor harmonic : T ST T T ST TST ST
# Minor melodic : T ST T T T T ST


def interval(a, b):
    semitones = ['CDb', 'C#D', 'D#E', 'DEb', 'EF', 'FGb', 'F#G', 'GAb', 'G#A', 'ABb', 'A#B', 'BC']
    whole_tones = ['CD', 'DE', 'FG', 'GA', 'AB', 'CbDb', 'DbEb', 'FbGb', 'GbAb', 'AbBb', 'BC#', 'EF#', 'C#D#', 'D#E#',
                   'F#G#', 'G#A#', 'A#B#', 'EbF', 'BbC']
    tone_and_half = ['CbD', 'CD#', 'DbE', 'DE#', 'EbF#', 'FbG', 'FG#', 'GbA', 'GA#', 'AbB', 'AB#', 'BbC#']
    c = a + b
    if c in semitones:
        return 1
    if c in whole_tones:
        return 2
    if c in tone_and_half:
        return 3


scale = []
tons = []
for e, c in enumerate(range(0, 8), start=1):
    scale.append(input(f'Type the {e}º note: ').title())
count_1 = 0
count_2 = 1
for c in range(0, 7):
    a = scale[count_1]
    b = scale[count_2]
    count_1 += 1
    if count_2 < 7:
        count_2 += 1
    tons.append(interval(a, b))
print('-' * (len(scale) * 5))
for c in range(1, 9):
    if c < 8:
        print(f'{c}º', end='-> ')
    else:
        print(f'{c}º')
for e, c in enumerate(scale):
    if e < 7:
        print(c, end=' -> ')
    else:
        print(c)

if tons == [2, 2, 1, 2, 2, 2, 1]:
    print(f'Major Scale')
if tons == [2, 1, 2, 2, 1, 2, 2]:
    print(f'Minor Scale')
if tons == [2, 1, 2, 2, 1, 3, 1]:
    print(f'Minor Harmonic Scale')
if tons == [2, 1, 2, 2, 2, 2, 1]:
    print(f'Minor Melodic Scale')

# Minor harmonic : T ST T T ST TST ST
# Minor melodic : T ST T T T T ST



