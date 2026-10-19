# sets
from pyscript import display, document #type:ignore

def action(e):
    input1 = document.getElementById('fn').value
    input2 = document.getElementById('ln').value


    grade7 = {'Bree Charlett Ambag', 'Loi Chee Punto'}

    grade8 = {'Montenegro Di Ampalaya', 'Nami Reguindo Sanginsing'}

    grade9 = {'Isaac Sheldon Nguyen', 'Paige Ten Fili'}

    grade10 = {'Gann Arkin O. San Agustin', 'Karter Anzas Juanito'}

    input3 = input1 + input2

    batch = grade7 | grade8 | grade9 | grade10
    batch.add(input3)

    number_ofMembers = len(batch)

    display(f'list of all members: {batch}', target='output')
    display(f'No. of members: {number_ofMembers}', target='output')