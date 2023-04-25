class Workers:
    def __init__(self, name, surname, salary):
        self.name = name
        self.surname = surname
        self.salary = salary
    
    def info(self):
        print(f'Worker {self.name}, surname {self.surname}, salary: {self.salary}')

class Administrator(Workers):
    def __init__(self, name, surname, salary):
        super().__init__(name, surname, salary)

class Director(Workers):
    def __init__(self, name, surname, salary, bonus):
        super().__init__(name, surname, salary)
        self.bonus = bonus
        self.salary += self.bonus
    
    def info(self):
        super().info() 
        print(f'With bonus, witch {self.bonus}')

worker1 = Workers('Jhon', 'Walker', 2000)
worker2 = Workers('James', 'Lenster', 2000)
worker3 = Administrator('Paul', 'Wales', 2500)
director = Director('Chris', 'Simpsons', 4000, 1000)

workers = [worker1, worker2, worker3, director]

for worker in workers:
    worker.info()
        
