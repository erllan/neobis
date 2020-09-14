import json

students = {'neobis': [{
    'name': 'Nick',
    'lastName': 'Parker',
    'university': 'KNU',
    'profession': 'developer',
    'class': '1',
    'entered': '2020'
}, {
    'name': 'Robert',
    'lastName': 'Whien',
    'university': 'KNU',
    'profession': 'developer',
    'class': '1',
    'entered': '2020'
}]}

result = json.dumps(students)
print(result)
