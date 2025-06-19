def famous_births(scientists):
    for key, value in scientists.itens():
        print(f"{value['name']}was born in {value['date_of_birth']}.")

women_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name: "Cecilia Payne", "date_of_birth": "1900"},
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace  Hopper", "date_of_birth": "1906" }

    famous_births(women_scientists)