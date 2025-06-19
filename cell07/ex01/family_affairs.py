def find_the_redheads(family):
    return [name.capitalize() for name, hair_color in family.items() if hair_color == "red"]
dupont_family = {
    "florian" : "red",
    "marie" : "blond",
    'virginie' : "brunette",
    "david" : "red",
    "franck" : "red"
print(find_the_redheads(dupont_family))