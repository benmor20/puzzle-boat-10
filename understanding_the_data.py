
from collections import Counter
from typing import *


class Person:
    def __init__(self, data_str: str):
        data_pts = data_str.split(';')
        self.first_name = data_pts[0]
        self.mi = data_pts[1]
        self.last_name = data_pts[2]
        self.age = int(data_pts[3])
        self.hair_color = data_pts[4]
        self.eye_color = data_pts[5]
        self.sisters = int(data_pts[6])
        self.brothers = int(data_pts[7])
        try:
            self.num_pets = int(data_pts[8])
        except ValueError:
            self.num_pets = -1
        self.pet_types = data_pts[9].split(', ')
        self.occupation = data_pts[10]
        self.education = data_pts[11].strip()
        if len(self.education) == 0:
            self.education = None
        self.note = data_pts[12].strip()
        if len(self.note) == 0:
            self.note = None

    def get_data(self, name: str) -> Union[str, int, List[str], None]:
        if name == 'First Name':
            return self.first_name
        if name == 'MI':
            return self.mi
        if name == 'Last Name':
            return self.last_name
        if name == 'Age':
            return self.age
        if name == 'Hair Color':
            return self.hair_color
        if name == 'Eye Color':
            return self.eye_color
        if name == 'Sisters':
            return self.sisters
        if name == 'Brothers':
            return self.brothers
        if name == 'No. of Pets':
            return self.num_pets
        if name == 'Types of Pets':
            return self.pet_types
        if name == 'Occupation':
            return self.occupation
        if name == 'Education':
            return self.education


def main():
    people = []
    with open('data/understanding_the_data.csv', 'r') as file:
        lines = file.readlines()
        for line in lines[1:]:
            people.append(Person(line))

    counters = {name: Counter() for name in lines[0].split(';')[:-1]}
    for person in people:
        for name in counters:
            data = person.get_data(name)
            if data is None or isinstance(data, list):
                continue
            if isinstance(data, int):
                counters[name].update([data])
            else:
                try:
                    counters[name].update([data[0]])
                except IndexError as e:
                    print(name, data)
                    raise e
    for name, counter in counters.items():
        print(f'{name} ({len(counter)}): {counter}')


if __name__ == '__main__':
    main()
