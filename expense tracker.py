#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json
import matplotlib.pyplot as plt

FILE_NAME="expenses.json"
exp_tracker={}

def show_graph():
    if not exp_tracker:
        print("no data found")
        return

    categories=list(exp_tracker.keys())
    totals=[sum(exp_tracker[c]) for c in categories]

    plt.figure()
    plt.title("expense Chart")
    plt.xlabel("category")
    plt.ylabel("total spent")
    plt.bar(categories,totals)
    plt.show()

def show_pie_chart():
    if not exp_tracker:
        print("no data found")
        return

    categories=list(exp_tracker.keys())
    totals=[sum(exp_tracker[c] )for c in categories]

    plt.figure()
    plt.title("spending distribution")
    plt.pie(totals,labels=categories , autopct="%1.1f%%")
    plt.show()


def load_data():
    global exp_tracker
    try:
        with open(FILE_NAME,"r") as f:
            exp_tracker =json.load(f)

        for c in exp_tracker:
            exp_tracker[c]=[float(x) for x in exp_tracker[c]]
            
        print("Data loaded successfully!")
        
    except FileNotFoundError:
        exp_tracker = {}
        print("No previous data found. Starting fresh.")

    except:
        exp_tracker = {}
        print("File corrupted. Starting fresh.")

def save_data():
    with open(FILE_NAME, "w") as f:
        json.dump(exp_tracker,f)
        print("Data saved successfully!")


load_data()

while True:
    print("\n Expense Tracker Menue")
    print("1  add expenses")
    print("2  category total")
    print("3  over all total")
    print("4  most spent category ")
    print("5 show graph")
    print("6  show pie chart")
    print("7 edit expenses")
    print("8 print expenses")
    print("9 end")
    

    choice=input("enter choice")
    
    if choice=="1":
        while True:
            spent=input("enter money spent (or 'end' to stop)")
            if spent.lower()=="end":
                break
                
            spent=float(spent)
            category=input("enter category")
            
            if category not in exp_tracker:
                exp_tracker[category]=[]

            
            exp_tracker[category].append(spent)
            save_data()
            print(exp_tracker)
        
    elif choice =="2":
        print("\ncategory total")
        for category , expenses in exp_tracker.items():
            print(category , "=" , sum(expenses))
    
    elif choice=="3":
        overall_total=sum(sum(expenses) for expenses in exp_tracker.values())
        print("\nover all total","=" ,overall_total)

    elif choice=="4":
        max_category=None
        max_amount=0
        for category , expenses in exp_tracker.items():
            total=sum(expenses)
            if total>max_amount:
               max_amount=total
               max_category=category
        print("\nmax amount :", max_category,"=",max_amount)

    elif choice =="5":
        show_graph()

    elif choice =="6":
        show_pie_chart()

    elif choice=="7":
        if not exp_tracker:
            print("no data")
            continue

        print("categories")
        for c in exp_tracker:
            print("-",c)

        categ=input("enetr category to edit")
        if categ not in exp_tracker:
            print("category not found")
            continue

        print(f"\nExpenses in '{categ}':")
        for i,e in enumerate(exp_tracker[categ]):
            print(f"{i}.Amount: {e}")
        idx=input("enter index of expense to edit")
        idx=int(idx)
        action = input("Type 'edit' to change or 'delete' to remove:").lower()

        if action=="edit":
            new_amount=float(input("enter new amount:"))
            exp_tracker[categ][idx]=new_amount
            save_data()
            print("Expense updated successfully")

        if action=="delete":
            exp_tracker[categ].pop(idx)
            save_data()
            print("deleted sucessfully")

    elif choice=="8":
        if not exp_tracker:
            print("no data")
        else:
            print("\navailable categories")
            for c in exp_tracker:
                print("-",c)

            category=input("enter category name")

            if category not in exp_tracker:
                print("Category not found")
            else:
                print("\nExpenses in",category,":")

                for amount in exp_tracker[category]:
                    print(amount)
        

    elif choice=="9":
        break 


    


# #### 
