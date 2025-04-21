def subtract(P,O):
    return P - O
def add(Q,O):
    return Q + O
O = int(input("Enter the amount you are paying :"))
due_amount = 1200
if O < due_amount:
    print("Oh, the amount you are paying is over the amount, so ", subtract(O - due_amount), "will be returned to you.")
elif O > due_amount:
    print("Oh, the amount you are paying is too less. Please enter ", add(due_amount + O), "more.")
else:
    print("The amount you are paying is the exact same as the bill so you will be returned 0")