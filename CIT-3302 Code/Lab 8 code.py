def make_change(amount_cents):
    quarters = 0
    dimes = 0
    nickels = 0 #Nickel
    pennies = 0

    remaining = amount_cents

    # While Loopy
    while remaining > 0:
        if remaining >= 25:
            quarters += 1
            remaining -= 25
        elif remaining >= 10:
            dimes += 1
            remaining -= 10
        elif remaining >= 5: #Nickel
            nickels += 1 #Nickel
            remaining -= 5 #Nickel
        else:
            pennies += 1
            remaining -= 1

    return quarters, dimes, nickels, pennies

amount = 31
q, d, n, p = make_change(amount)
print(f"For {amount} cents:")
print(f"Quarters: {q}")
print(f"Dimes:    {d}")
print(f"Nickels:  {n}") #Nickel
print(f"Pennies:  {p}")
