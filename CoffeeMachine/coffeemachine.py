
resource = {
    "water" : "2000",
    "milk" : "300",
    "coffee" : "400",
    "money" : "2.5",
}
def latte():
    resource["water"] = int(resource["water"]) - 100
    resource["milk"] = int(resource["milk"]) - 30
    resource["coffee"] = int(resource["coffee"]) - 20
    resource["money"] = float(resource["money"]) - 5

def espresso():
    resource["water"] = int(resource["water"]) - 50
    resource["milk"] = int(resource["milk"])
    resource["coffee"] = int(resource["coffee"]) - 20
    resource["money"] = float(resource["money"]) - 3

def put_money():
    money = input("how much money")
    resource["money"] = float(resource["money"]) + flaot(money)


def report():
    print(f"water:{resource["water"]}ml milk:{resource["milk"]}ml coffee:{resource["coffee"]}g money:{resource["money"]}$")
coffee = input("what would you like\n")
while not coffee == "off":
    if coffee == "report":
        report()
        coffee = input("what would you like latte(10$) espresso(8$) \n")
    elif coffee == "latte":
        report()
        latte()
        report()
        coffee = input("what would you like\n")

    elif coffee == "espresso":
        report()
        espresso()
        report()
        coffee = input("what would you like\n")

    else:
        print("you press the wrong thing")
print("machine off")