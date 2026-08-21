raw_delivery = [("Apple", 0.75, 50), 
                ("Banana", 0.40, 100),
                ("Milk", 2.50, 15),
                ("Bread", 1.80, 20), 
                ( "Apple", 0.75, 30),]

shopping_cart= ["Apple", "Apple", "milk","Bread","Dragunfruit"]

def build_inventory(delivery):
    inventory = {}
    for name,price,qty in delivery:
        if name in inventory:
            inventory[name]["stock"]=inventory[name]["stock"]+qty
        else:
            inventory[name]={"price":price, "stock":qty}
    return inventory

def checkout(inventory,cart):
    receipt=[]
    total=0

    for item in cart:
        if item not in inventory:
            print(f"{item} is not carried in the store")
        elif inventory[item]["stock"]==0:
            print(f"{item} is sold out")
        else:
            inventory[item]["stock"] -=1
            receipt.append((item,inventory[item]["price"]))
            total += inventory[item]["price"]
    return receipt,total

inventory = build_inventory(raw_delivery)
receipt, total = checkout(inventory,shopping_cart)

print("\n---Receipt---")
for name,price in receipt:
    print(f"{name}-{price}")

print(f"Total={total}")
