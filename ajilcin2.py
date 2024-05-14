class Ajilchin:
    def __init__(self, f_name, l_name, id, gender, age, worked_year, still_working, salary, role):
        self.Нэр = f_name
        self.Овог = l_name
        self.id = id
        self.Хүйс = gender
        self.нас = age
        self.АжилсанЖил = worked_year
        self.АжиллажБайгаа = still_working
        self.Цалин = salary
        self.АлбанТушаал = role //12
        
    def __str__(self):
        return f"{self.Нэр} -ийн {self.Овог} нь {self.АжилсанЖил} жил ажилласан. (Ажиллаж байгаа эсэх: {self.АжиллажБайгаа} нас: {self.нас} Хүйс: {self.Хүйс} Цалин: {self.Цалин} Албан тушаал: {self.АлбанТушаал})"

def read_workers_from_file(filename):
    workers = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            data = line.strip().split(',')
            workers.append(Ajilchin(*data))
    return workers

def filter2(workers, filename):
    with open('dar.txt', 'w', encoding='utf-8') as f:
        for worker in workers:
            f.write(str(worker) + '\n')
    print("Амжилттай хадгалсан")

    with open(filename, 'w', encoding='utf-8') as file:
        pass
    print(f"{filename} has been emptied successfully.")
    
    with open('dar.txt', 'r', encoding='utf-8') as f:
        print(f.read())
        
    result = workers
    while True:
        filter_value = input("leave or save")
        if filter_value.lower() == 'leave':
            break
        elif filter_value.lower() == 'save':
            with open('dar.txt', 'w', encoding='utf-8') as f:
                for worker in result:
                    f.write(str(worker) + '\n')
            print("Амжилттай")
            break

        new_result = []
        for worker in result:
            if filter_value.lower() in [str(value).lower() for value in vars(worker).values()]:
                new_result.append(worker)

        result = new_result

        i = 0
        for worker in result:
            i += 1
            print(f"{i}. {vars(worker)}\n")

    return result
    

def main():
    filename = 'UbA.txt'
    workers = read_workers_from_file(filename)
    filter2(workers, filename) 

if __name__ == "__main__":
    main()
