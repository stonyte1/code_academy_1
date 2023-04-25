column = list('ABCDEFGH')
lines = list(range(1, 9))

print('  ', end='')

# All letter are being drawn
for letter in column:
    print(letter, end=' ')
print('')
# First line number is chosen
for line_nr in lines:
    print(line_nr, end=' ')
    # For line nr is set for each letter and we print black or white rectangule
    for column_line_nr, letter in enumerate(column):
        # Here is choosen that in unequal line white rectangule is drawn every two steps from B letter.
        # And here is choosen that in equal line white rectangule is drawn every two steps from A letter.
        if (line_nr % 2 == 0 and column_line_nr % 2 == 0) or \
        (line_nr % 2 == 1 and column_line_nr % 2 == 1):
            print('\u25A0', end= ' ')
        else:
            print(' ', end=' ')
    print('')
