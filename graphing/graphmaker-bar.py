#!/usr/bin/env python3

import matplotlib.pyplot as plt

def main():
    
    print("Let's make the actual perfect pizza");
    topping = 0
    toppings = []
    amount = []
    while topping < 4 :
        top = input("Please enter your topping: ")
        toppings.append(top)
        am =float(input("Please enter the percentage for this topping: "))
        amount.append(am)
        topping += 1
    print(toppings)
    print(amount)

    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = toppings[0], toppings[1], toppings[2], toppings[3]
    sizes = [amount[0], amount[1], amount[2], amount[3]]
    explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    
    plt.savefig("/home/student/mycode/graphing/perfectPizza.png")
    plt.savefig("/home/student/static/perfectPizza.png")


if __name__ == "__main__":
    main()

