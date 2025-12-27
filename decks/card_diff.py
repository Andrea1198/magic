import os

deck_filenames = os.listdir("./inputs/")

all_qties = []
all_cards = []

for deck in deck_filenames:
    
    qties = []
    card_names = []
    with open("./inputs/" + deck) as f:
        cards = f.readlines()
        for i in range(len(cards)):
            if len(cards[i].split()) < 2 or cards[i].split()[0] == "//":
                continue
            cards[i] = cards[i].split("(")[0]
            qties.append(int(cards[i].split()[0]))
            card_names.append(' '.join(cards[i].split()[1:]).lower())
        print(qties)
        for i in range(len(qties)):
            qty = int(qties[i])
            card = card_names[i]
            for j in range(i+1,len(qties)):
                qty2 = int(qties[j])
                card2 = card_names[j]
                if card == card2:
                    qties[i] = qty + qty2
                    qties[j] = 0
        
        i = len(qties)-1
        print(qties)
        while i >= 0:
            if qties[i] == 0:
                qties.pop(i)
                card_names.pop(i)
                print(qties)
            i -= 1
        print(qties)
        all_qties.append(qties)
        all_cards.append(card_names)

if not os.path.isdir("common_cards"):
    os.makedirs("common_cards")

if not os.path.isdir("diff_cards"):
    os.makedirs("diff_cards")

count = []
q = 0
for i in range(len(all_qties)):
    for j in range(i+1, len(all_qties)):
        with open("common_cards/" + deck_filenames[i] + " vs " + deck_filenames[j] + ".txt", "w") as f:
            count.append(0)
            for k1, c1 in enumerate(all_cards[i]):
                for k2, c2 in enumerate(all_cards[j]):
                    if c2 == c1:
                        f.write(str(min(all_qties[i][k1], all_qties[j][k2])) + " " + c1 + "\n")
                        count[q] += int(min(all_qties[i][k1], all_qties[j][k2]))
            q += 1

q = 0
for i in range(len(all_qties)):
    for j in range(i+1, len(all_qties)):
        with open("diff_cards/" + deck_filenames[i] + " vs " + deck_filenames[j] + ".txt", "w") as f:
            for k1, c1 in enumerate(all_cards[i]):
                if c1 not in all_cards[j]:
                    f.write(str(all_qties[i][k1]) + " " + c1 + "\n")
                    count[q] += int(all_qties[i][k1])
                else:
                    for k2, c2 in enumerate(all_cards[j]):
                        if c1 == c2:
                            if abs(int(all_qties[i][k1]) - int(all_qties[j][k2])) != 0:
                                f.write(str(abs(int(all_qties[i][k1]) - int(all_qties[j][k2]))) + " " + c1 + "\n")
                                count[q] += abs(int(all_qties[i][k1]) - int(all_qties[j][k2]))
            q += 1
print(count)

