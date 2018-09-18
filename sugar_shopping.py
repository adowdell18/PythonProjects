#Author: Angie Dowdell
#Date: February 9, 2016


weight_package_1 = eval(input("Please enter the weight of package 1 of sugar in oz: "))
price_package_1 = eval(input("Please enter the price of package 1 of sugar in dollars: "))

weight_package_2 =eval(input("Please enter the weight of 2 package of sugar in oz: "))
price_package_2 = eval(input("Please enter the price of package 2 of sugar in dollars: "))

if (price_package_1/weight_package_1)< (price_package_2/weight_package_2):
    print("Package 1 has the better price")
                       
elif (price_package_1/weight_package_1)> (price_package_2/weight_package_2):
    print("Package 2 has the better price")

else:
    print("Package 1 and package 2 have an equivalent value.")
                       
