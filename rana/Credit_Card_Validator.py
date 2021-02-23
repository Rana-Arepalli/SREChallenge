import re
def validate_credit_cards(credit_cards):
    valid_structure = r"[456]\d{3}(-?\d{4}){3}$"
    no_four_repeats = r"((\d)-?(?!(-?\2){3})){16}"
    filters = valid_structure, no_four_repeats

    for cc in credit_cards:
        if all(re.match(f, cc) for f in filters):
            print("Valid")
        else:
            print("Invalid")

credit_cards = []
n = int(input())
for _ in range(n):
    eachNumber = raw_input().strip()
    credit_cards.append(eachNumber)
validate_credit_cards(credit_cards)