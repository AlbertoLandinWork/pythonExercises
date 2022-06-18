from typing import Dict, List, Tuple

positives: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

users: Dict[str, int] = {
    'Mexico' : 1,
    'Argentina' : 3,
    'Colombia' : 4
}

countries: List[Dict[str, str]] = [
    {
        'Name' : 'Argentina',
        'People' : '5000'
    },
    {
        'Name' : 'Mexico',
        'People' : '9000,000'
    },
    {
        'Name' : 'Colombia',
        'People' : '50000000000'
    },
]

numbers: Tuple[int, float, int] = (1, 1.5, 2)

CoordinatesType = List[Dict[str, Tuple[int, int]]]

coordinates: CoordinatesType = [
    {
        'coord1' : (1, 2),
        'coord2' : (3, 4)
    },
    {
        'coord1' : (5, 6),
        'coord2' : (7, 8)
    },
]

def suma(a: int, b: int) -> int:
    return a + b

print(suma('1', '2'))