products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}

def get_product(code):
    return products[code]

get_product("espresso")

def get_property(code, property):
    return products[code][property]

get_property("espresso", "price")

def main():

    products = []
    americano = 0
    brewedcoffee = 0
    cappuccino = 0
    dalgona = 0
    espresso = 0
    frappuccino = 0
    session = True

    while (session == True):
        order = input("Please input the customer's order following this format: 'product_code, quantity'. Once done, input a slash: '/'")
        if order == "/":
            break
        else:
            product_code = order.split(",")[0]
            quantity = order.split(",")[1]

            if product_code not in products:
                products.append(product_code)

            if product_code == "americano":
                americano += int(quantity)
            elif product_code == "brewedcoffee":
                brewedcoffee += int(quantity)
            elif product_code == "cappuccino":
                cappuccino += int(quantity)
            elif product_code == "dalgona":
                dalgona += int(quantity)
            elif product_code == "espresso":
                espresso += int(quantity)
            elif product_code == "frappuccino":
                frappuccino += int(quantity)
            else:
                continue

    products.sort()

    for i in range(len(products)):
        if products[i] == "americano":
            get_product("americano")["quantity"] = americano
        elif products[i] == "brewedcoffee":
            get_product("brewedcoffee")["quantity"] = brewedcoffee
        elif products[i] == "cappuccino":
            get_product("cappuccino")["quantity"] = cappuccino
        elif products[i] == "dalgona":
            get_product("dalgona")["quantity"] = dalgona
        elif products[i] == "espresso":
            get_product("espresso")["quantity"] = espresso
        elif products[i] == "frappuccino":
            get_product("frappuccino")["quantity"] = frappuccino

    with open("receipt.txt","w") as receipt:
        total = 0
        receipt.write('''
==
"CODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL"''')

        for i in range(len(products)):
            product_code = products[i]
            name = get_property(product_code,"name")
            finalquantity = int(get_property(product_code,"quantity"))
            subtotal = finalquantity * get_property(product_code,"price")
            total += subtotal

            if product_code == 'dalgona':
                receipt.write(f'\n{product_code}\t\t\t{name}\t\t\t{finalquantity}\t\t\t\t{subtotal}')
            else:
                receipt.write(f'\n{product_code}\t\t{name}\t\t{finalquantity}\t\t\t\t{subtotal}')

        receipt.write(f'\nTotal:\t\t\t\t\t\t\t\t\t\t{total}\n==')

main()
