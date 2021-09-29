from typing import Iterator
from typing import List
from typing import Union
from collections.abc import Iterable
from typing import Optional
from collections import namedtuple
from typing import Dict

animals = [
    {
        'name': 'lion',
        'size': 'medium'
    },
    {
        'name': 'spider',
        'size': 'little'
    },
    {
        'name': 'platypus',
        'size': 'medium'
    }
]

a: Dict[str, int] = {'fer': 10, 'otro': 20}


def get_animals(amount: int) -> Iterator[dict]:
    for i in range(amount):
        yield animals[i]


def find_by_name(name: str) -> Union[dict, None]:
    for i, animal in enumerate(animals):
        if animal['name'] == name:
            return animal

    return None


def find_by_size(size: str = 'little') -> list:
    filtered = [animal for animal in animals if animal['size'] == size]
    return filtered


def create_group(*args: int) -> list:
    group = []
    for i in args:
        group.append(animals[i])
    return group


def add_animals(names: List[str]) -> None:
    for name in names:
        animals.append({name: name})


def fed_animal(animal: dict) -> None:
    print('feeding ' + animal['name'])


def fed_animals(names: List[str]) -> None:
    for name in names:
        animal = find_by_name(name)
        if animal is not None:
            fed_animal(animal)


Helper = namedtuple('Helper', 'name age')


def assign_animal(animal: dict, helper: Helper) -> None:
    animal['helper'] = helper


if __name__ == '__main__':
    fed_animals(['lion','elephant'])