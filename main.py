# Created by Cole Hersowitz
# Tool for generating test stripe tokens and using Stripe

import stripe

command = ""

stripe.api_key = "YOUR STRIPE KEY"

def createToken():
    tok = stripe.Token.create(
        card={
            "number": '4242424242424242',
            "exp_month": 12,
            "exp_year": 2017,
            "cvc": '123'
        },
    )
    return tok["id"]

def recentCharges():
    charges = stripe.Charge.list(limit=10)

    results = []
    for charge in charges["data"]:
        item = {
            "amount": (charge["amount"])/100,
            "customer": charge["customer"],
            "description": charge["description"],
            "id": charge["id"]
        }
        results.append(item)
    return results

def testCharge():
    token = createToken()
    charge = stripe.Charge.create(
        amount=100,  # amount in cents, again
        currency="usd",
        source=token,
        description="test charge"
    )
    return charge

while "exit" != command:
    command = input("$").strip()

    if command == "generate token":
        result = createToken()
        print("Token: ", result)
    elif command == "ls charges":
        result = recentCharges()
        print("Charges: ")
        for i in range(len(result)):
            print("Charge " + str(i) + ":")
            print("   id: ", result[i]["id"])
            print("   amount: ", result[i]["amount"])
            print("   customer: ", result[i]["customer"])
            print("   description: ", result[i]["description"])
    elif command == "test charge":
        result = testCharge()
        print("Test Charge: ", result)


else:
    import sys
    sys.exit()
