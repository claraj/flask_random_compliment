import random

compliments = [
    { 'text': 'You look nice today!' },
    { 'text': 'Your program is really good!' },
    { 'text': 'You deserve to have a great day today!' },
    { 'text': 'It\'s so fun to code with you!' },
]

def random_compliment():
    return random.choice(compliments)
