import operator

def person_lister(f):
    def inner(people):
        # complete the function
        # Создаем список кортежей (индекс, возраст, человек)
        # для сохранения исходного порядка при одинаковом возрасте
        indexed_people = [(i, int(person[2]), person) for i, person in enumerate(people)]

        # Сортируем по возрасту и исходному индексу
        sorted_people = sorted(indexed_people, key=lambda x: (x[1], x[0]))

        # Применяем форматирование к отсортированным людям
        return [f(person[2]) for person in sorted_people]
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')
