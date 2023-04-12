# vartotojo_vardas = input('Iveskite savo varda:')
# vartotojo_amzius = input('Iveskite savo amziu:')

# vartotojo_amzius100 = 100 - int(vartotojo_amzius)

# print("Jusu vardas {}, jums sueis 100 metu po {} metu.".format(vartotojo_vardas, vartotojo_amzius100))

# vartotojo_ugis = input('Iveskite ugi (cm):')
# vartotojo_ugism = int(vartotojo_ugis) / 100

# print('Ugis (cm): {}/n Ugis (m): {}'.format(vartotojo_ugis, vartotojo_ugism))

# vartotojo_atlyginimas = input('Iveskite atlyginima:')
# menesinis_mokescio_atskaitymas = (int(vartotojo_atlyginimas) * 21) / 100
# menesinis_atlyginimas = int(vartotojo_atlyginimas) - menesinis_mokescio_atskaitymas


# print(f'Menesinis talyginimas po mokesciu: {menesinis_atlyginimas:.0f}')

parinkimas = input('Jei norite temperatura keisti i Celsijus rasykite c, jei i Farenheitus rasykite f:')
temperatura = input('Iveskite temperatura, kuria norite konvertuoti:')

if parinkimas == 'c':
    atsakymas = (float(temperatura) - 32) * (5/9)
    print(f'Temperatura Celsijum: {atsakymas}')
elif parinkimas == 'f':
    atsakymas = (float(temperatura) * (9/5)) + 32
    print(f'Temperatura Farenheito: {atsakymas}')

print('Veikia')