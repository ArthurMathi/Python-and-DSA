# # Pizza bill Generater

# def pizza_bill_generator():
#     pizza_prices = {
#         "Normal": {
#             "Veg": 250,
#             "Non-Veg": 350
#         },
#         "Delux": {
#             "Veg": 400,
#             "Non-Veg": 550
#         }
#     }
    
#     extra_charges = {
#         "Extra Cheese": 50,
#         "Extra Topping": 75,
#         "Take Away": 20,
#         "Water Bottle": 20,
#         "Ketchup": 10,
#         "Soft Drinks": 60
#     }
    
#     print("=" * 50)
#     print("          PIZZA BILLING SYSTEM")
#     print("=" * 50)
    
#     total_bill = 0
#     pizzas_ordered = []
    
#     while True:
#         print("\n--- ORDER PIZZA ---")
#         print("Categories: 1. Normal  2. Delux")
#         category_choice = input("Select Category (1/2): ").strip()
        
#         if category_choice == "1":
#             category = "Normal"
#         elif category_choice == "2":
#             category = "Delux"
#         else:
#             print("Invalid choice! Try again.")
#             continue
        
#         print("\nType: 1. Veg  2. Non-Veg")
#         type_choice = input("Select Type (1/2): ").strip()
        
#         if type_choice == "1":
#             pizza_type = "Veg"
#         elif type_choice == "2":
#             pizza_type = "Non-Veg"
#         else:
#             print("Invalid choice! Try again.")
#             continue
        
#         price = pizza_prices[category][pizza_type]
#         print(f"\n✓ {category} {pizza_type} Pizza: ₹{price}")
        
#         pizzas_ordered.append((category, pizza_type, price))
#         total_bill += price
        
#         more_pizza = input("\nOrder another pizza? (yes/no): ").strip().lower()
#         if more_pizza != "yes":
#             break
    
#     print("\n" + "=" * 50)
#     print("--- ADD EXTRAS ---")
#     print("=" * 50)
    
#     while True:
#         print("\nAvailable Extras:")
#         for i, extra in enumerate(extra_charges.keys(), 1):
#             print(f"{i}. {extra}: ₹{extra_charges[extra]}")
#         print(f"{len(extra_charges) + 1}. No More Extras")
        
#         extra_choice = input("Select Extra (or skip): ").strip()
        
#         if extra_choice == str(len(extra_charges) + 1):
#             break
        
#         try:
#             choice_idx = int(extra_choice) - 1
#             extra_list = list(extra_charges.keys())
            
#             if 0 <= choice_idx < len(extra_list):
#                 extra_name = extra_list[choice_idx]
#                 extra_price = extra_charges[extra_name]
#                 total_bill += extra_price
#                 print(f"✓ Added {extra_name}: ₹{extra_price}")
#             else:
#                 print("Invalid choice! Try again.")
#         except ValueError:
#             print("Invalid input! Try again.")
    
#     print("\n" + "=" * 50)
#     print("          FINAL BILL")
#     print("=" * 50)
    
#     pizza_subtotal = sum(price for _, _, price in pizzas_ordered)
#     extras_total = total_bill - pizza_subtotal
    
#     print("\nPizzas Ordered:")
#     for i, (cat, ptype, price) in enumerate(pizzas_ordered, 1):
#         print(f"  {i}. {cat} {ptype} Pizza: ₹{price}")
    
#     print(f"\nPizza Subtotal: ₹{pizza_subtotal}")
    
#     if extras_total > 0:
#         print(f"Extras Total: ₹{extras_total}")
    
#     print("-" * 50)
#     print(f"TOTAL BILL: ₹{total_bill}")
#     print("=" * 50)
    
#     return total_bill

# if __name__ == "__main__":
#     pizza_bill_generator()


# code
# stack=[]

# while True:
#     print("\n1. Push 2.Pop 3.Peak 4.Display 5.Exit")
#     choice=int(input("Enter Choice:"))
#     if choice==1:
#         val=int(input("enter value"))
#         stack.append(val)
#         print("Pushed",val)
#     elif choice == 2:
#         if not stack:
#             print("Stack Empty")
#         else:
#             print("popped",stack.pop())
#     elif choice ==3:
#         if not stack:
#             print("stack empty")
#         else:
#             print("Top")  
#     elif choice==4:
#         print("STack",stack)
#     else:
#         print("invalid choice")                          
    


# Queue
queue=[]
while True:
    print("\n1.Enqueue 2.DeQueue 3.Peak 4.Display 5.Exit")
    choice=int(input("Enter Choice:"))
    if choice==1:
        val=int(input("enter value"))
        queue.append(val)
        print("Added",val)
    elif choice == 2:
        if not queue:
            print("Queue Empty")
        else:
            print("Removed",queue.pop())
    elif choice ==3:
        if not queue:
            print("queue empty")
        else:
            print("Top")  
    elif choice==4:
        print("queue",queue)
    else:
        print("invalid choice")              

#Circular Queue 
# 1)reuse empty Speces-
# Save memory
# if frount is free ,rear can resue it

n=3
queue[rear]=10
rear=(rear+1)%size

       [10 - - - - - ]
[10,20 - - - ] 
[10,20,30 - -]
delete -> 10 

[-20 30 - - ]

Pseudocode
ENQUEUE

.