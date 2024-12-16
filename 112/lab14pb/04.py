# get chem formula
# get target

# make dict for store key each 

"""
atoms = {
    [element] = count
}
"""

"""
Fe3H2Na2O45Si
Sr2RuO4
CoC2O4
C17H19N3O3S
CH3COOH
"""

def get_element_count(chem_formula:str, target_atom):
    elements = {}

    st = ''

    for char in chem_formula:
        if char.isupper() and st == '':
            st += char
        elif char.isupper() and st != '':
            if st not in elements:
                elements[st] = '1'

            st = char
        elif char.islower():
            st += char
        else:
            if st not in elements:
                elements[st] = ''

            elements[st] += char

    last_index = chem_formula.rfind(st)
    if last_index == len(chem_formula) - len(st):
        elements[st] = 1

    return elements.get(target_atom, 0)

chem_formula = input()
target_atom = input()

print(get_element_count(chem_formula, target_atom))