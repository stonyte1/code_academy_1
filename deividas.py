
print("Labas!")
vardas = str(input("Iveskite prašau savo vardą: "))
metai = int(input("Įveskite prašau kiek Jums metų: "))
if metai <= 18:
    print(vardas, " tu dar mailius.")
elif metai <=25:
    print(vardas, " tu jau beveik savarankiskas mailius.")
elif metai <=35:
    print(vardas, " sveikinu jau tikriausiai gyveni savarankiskai ir nebepriklausomas nuo mamos!")
elif metai <=38:
    print(vardas, ' jau visai netoli 39 metai!')
elif metai == 39:
    print(vardas, "paklausyk cia kaip tik tau https://www.youtube.com/watch?v=GRVxtODhTM0")
elif metai <=60:
    print(vardas, " sveikinu su vidurio amziaus krize")
elif metai <=70:
    print(vardas, " issvajotaji pencija kuria atimineja anukai?")
else: 
    print(vardas, " zinai esu priverstas lenkti galva pries tave senoli! ")
print(vardas, " nors tau ir", metai, "tu vistiek esi nuostabus zmogus, o si programa sukurta for fun !")
