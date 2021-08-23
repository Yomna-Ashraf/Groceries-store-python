groceries = {
    "cheese":{"mozzrilla":[10,10],"parmesan":[0,4],"french cheese":[3,20]},
    "biscuits":{"oreo":[20,2],"lotus":[4,5]},
    "vegitable":{"carrots":[10,3],"cucamber":[9,5],"lettuce":[14,3],"tomato":[12,6]},
    "fruits":{"apple":[9,8],"kiwi":[5,30],"mango":[9,13],"banana":[10,5]},
    "snacks":{"lollipop":[30,2],"chips":[40,5],"gum":[10,1]}
}
pill = []
products=[]
num_customers=[]
total=0
while len(num_customers) < 2:
    name = input("hello sir what is your name: ")
    while True:

        category=input("HI,What would you like to have,Sir?  ")
        if category  == "nothing":
            print("Thanks!")
            break
        elif category not in groceries:
            print(f"sorry we don't sell {category} in our market, please chhose something else: ")
        else:
            order=input(f"What kind of {category} would you like to have,Sir? ")
            if  order == "nothing":
                print("Thanks!")
                print(" ")
                break
            else:
                if order not in groceries[category]:
                    print(f"Sorry we are out of any {order}, Please, choose something else.")
                elif groceries[category][order][0] == 0:
                    print(f"sorry we are out of any {order} ")
                else:
                    quant = int(input("what are the quantity you want? "))
                    if quant > groceries[category][order][0]:
                        print(f"sorry we only have {groceries[category][order][0]} {order}")
                        answer = input("would you like to take those only? ")
                        if answer == "no":
                            print("ok")
                        else:
                            money = groceries[category][order][0] * groceries[category][order][1]
                            print(f"we added {groceries[category][order][0]} {order} to your pill")
                            groceries[category][order][0]=0
                            pill.append(money)
                            products.append(order)
                            
                    else:
                        money = quant * groceries[category][order][1]
                        groceries[category][order][0]=groceries[category][order][0]-quant
                        pill.append(money)
                        products.append(order)
                        print(f"we added {quant} {order}s to your pill")
    pill1 = sum(pill)
    pill=[]
    if pill1 == 0 :
        print("Sorry we coudn't help you! Please,visit our market later.")
    elif pill1>100:
        print("you bought: ")
        for i in products:
            print(f"  - {i}")
        print("Cheer up! you have 10% discount.")
        pill1 = pill1 - pill1*0.15
        print(f"your pill is {pill1} LE.")
        num_customers.append(name)
        total=total+pill1
        pill1 = 0

    else:
        print("you bought: ")
        for i in products:
            print(f"  - {i}")
        print(f"your pill is {pill1} LE.")

        num_customers.append(name)
        total=total+pill1
        pill1=0
    products=[]
print("MARKET CLOSED!")  
print(f"the num ber of customes for  today is {num_customers}")
print(f"the total amount of money earned today is {total}")