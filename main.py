# file = open('pakeitimai.txt', 'w+')
# file.write('Tavo tevas Tavo mama')
# file.seek(0)
# file_read = file.read()
# file_read = file_read.swapcase()
# print(file_read)
# file.close()

# file = open('skaiciai.txt', 'w')
# for i in range(1, 101):
#     file.write(str(i))
#     file.write('\n')

# file.close()

# file = open('tekstas.txt', 'w+')
# text = 'Kad tave sikanti sutrauktu, ir mieganti paimtu.'
# lenght = len(text) // 2
# file.write(text)
# file.seek(lenght)
# file_read = file.read()
# print(file_read)
# file.close()

file = open('eilutes.txt', 'w')
file.write('Saulėlydis žėri žemę švelniai.\nVakare vėjas šnypščia medžius.\nVėjas nerimsta, šnypščia ir švilpia.')
file.write('\n\nEvelina Stonytė')
file.close()

file = open('eilutes.txt', 'r')
for line in file:
    if 'vėjas' or 'Vėjas' in line:
        print(line)

file.close()
