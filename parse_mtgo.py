missing_exp = [
    "Ademi of the Silkchutes",
    "Spectral Restitching",
    "Cren, Undercity Dreamer",
    "Goben, Gene-Splice Savant", 
    "Nia, Skysail Storyteller",
    "Makdee and Itla, Skysnarers"
]

with open("./cube.txt", "r") as file:
    cube_cobra = file.readlines()

with open("./arriving.txt", "r") as file:
    arriving = file.readlines()

with open("./owned.txt", "r") as file:
    owned = file.readlines()

# Cards in cube_cobra not in arriving or owned
to_print = []
for card in cube_cobra:
    card_name = card.split(" (")[0].strip()
    found = False
    for line in arriving + owned:
        if card_name in line:
            found = True
            break
    if not found:
        to_print.append(card_name)

for card in missing_exp:
    to_print.append(card)

with open("./to_print.txt", "w") as file:
    for card in to_print:
        file.write(card + "\n")

with open("./cube_cobra.txt", "r") as file:
    cube_cobra = file.readlines()

with open("./to_print.txt", "r") as file:
    out = file.readlines()

# Check if owned + out + arriving covers cube_cobra
all_owned = owned + out + arriving
missing = []
for card in cube_cobra:
    card_name = card.split(" (")[0].strip()
    found = False
    for line in all_owned:
        if card_name in line:
            found = True
            break
    if not found:
        missing.append(card_name)

for card in missing:
    print(card)
