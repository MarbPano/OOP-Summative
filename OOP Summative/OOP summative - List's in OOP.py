#---------------#
#Summative Unit 4 - Dictionaries Program
#keeping track of expenses program
#By Marb Pano
#April 14, 2023
#---------------#

import random
import time 


#----dictionaries---#

employee_salary = {
    }#name of employee and thier salary

operating_cost = {'Rent': 0,
                  'Accounting and Legal Fees': 0,
                  'Bank Charges': 0,
                  'Sales Fees': 0,
                  'Marketing Fees': 0,
                  'Officce Supplies': 0,
                  'Repairs': 0,
                  'Utilities': 0,
                  
                  
    }
#other expenses like banking fees,accouting fees, marketing, office supplies.etc

product_cost = {
    }#how much did it cost to buy the product(s)



#---list---#
inspirational_words = ['If your going through a rough patch, just know everything will be alright we all been there!',
                       'People love you and you know it.',
                       'You can do this!',
                       'You are important',
                       'NEVER GIVE UP!',
                       'Your Business is doing good',
                       'Sales up, share prices down, life is good',
                       'A Rescession is bad... but not for investors',
                       'Invest Wisely!',
                       'Invest in my Crypto Pump and Dump(totes not a scam)',
                       'If you were told to invest in a Crypto Pump and Dump, dont do it!',
                       
]#when working on your business it is important we have inspirational words to help you through the day
#------inspiration-------#
def random_inspirational_words():
    x = random.choice(inspirational_words)
    print(f'    {x}')
#classess    
class Employee_salary:
    
    def __init__(self, employee_salary):
        self.employee_salary = employee_salary
        
        
    def print_things(self):
        print('')
     
        for item, cost in list(self.employee_salary.items()):
            print(f"{item}: ${cost}")
            
    def adding_things(self):
        print(" ")
        
        while True:#the only problem with this is that if you have two employees with the same name, the more recent input employee
            #will overwrite the previous ones value
            try:
                item = input("Emplyee Name(type 'done' if you finish): ")#the key in dictionary
                
                if item == 'done':
                    break
                
                
                else:
                    cost = float(input("Salary: "))#value of the dictionary
                    self.employee_salary[item] = cost
                    
                print("")   
                print("Contains:")
                self.print_things()
        
            except:
                print("ONLY USE NUMBERS(RESTART)")
                
    def remove_things(self):
        print("")
        
        while True:
            self.print_things()
        
            employee = input('What Employee/Salary do you want removed?(Type "done" to exit) ')
            
            if employee == 'done':
                break
         
            else:
                if employee in self.employee_salary:
                    del self.employee_salary[employee]#deletes the key along with value
                    self.print_things()
                 
                else:
                    print(f"{employee} is not in the Employee List")
        
        



class Operating_cost:
    
    def __init__(self, operating_cost):
        self.operating_cost = operating_cost
        
    def print_things(self):
        print("")
        
        for item, cost in list(self.operating_cost.items()):#for every item and cost in shopping_list print the {item} or key, {cost} or value. in dict
            print(f"{item}: ${cost}")
        
    def adding_things(self):
        print("")
        
        while True:
            
            try:
                for item, cost in list(self.operating_cost.items()):
                    
                    x = float(input(f"Overall cost of {item} "))
                    self.operating_cost[item] = x#i just wanted the value to change and not the set key
                
                print("")
                print("Contains")
                self.print_things()
                break# this is to exit out of the loop
                
            except:
                print("ONLY USE NUMBERS") 
        
        
    def remove_things(self):
        print("")#i WANTED only the value to be "removed" and not the key
        
        while True:
            
            self.print_things()
            
            expense = str(input('What Expense do you want removed?(Type "done" to exit) '))
            
            if expense == "done":#prety self explanatory
                break
            
            else:
                if expense in self.operating_cost: 
                    self.operating_cost[expense] = 0#essentially not removing the value and making it "None" but change value to 0
                    #this allows for math to be done, important for calc the net income
                    
                else:
                    print(f"{expense} is not in the Operating Cost") #fool proof
            
            print("") 
            
            self.print_things()#print often to show what is in list and what happen
            print("")
    
        
class Product_cost:
    
    def __init__(self, product_cost):
        self.product_cost = product_cost
    
    def print_things(self):
        print("")
        
        for item, cost in list(self.product_cost.items()):
            print(f"{item}: ${cost}")
        
        
    def adding_things(self):
        print(" ")
        
        while True:
            try:
                item = input("Product Name(type 'done' if you finish): ")#the key in dictionary
                
                if item == 'done':
                    break
                
                
                else:
                    cost = float(input("Cost of Product: "))#value of the dictionary
                    self.product_cost[item] = cost
                    
                print("")   
                print("Contains:")
                self.print_things()
        
            except:
                print("ONLY USE NUMBERS")
                
            
    def remove_things(self):
        print("")
        
        while True:
            self.print_things()
            
            product = input('What Product do you want removed?(Type "done" to exit) ')#asking for specific key in dic
            
            if product == 'done':#i used your model so that whenever done is typed, it goes out of the loop 
                break
            
            else:
                if product in product_cost:
                    del product_cost[product]#dont wanna make it too hard, so its better to just remove the key
                    self.print_things()#i like to print the dict often to show user whats there and what was removed
                    
                else:
                    print(f"{product} is not in the Product Cost") 
            
    
     
#Important Variables
ES = Employee_salary(employee_salary)
OC = Operating_cost(operating_cost)
PC = Product_cost(product_cost)

def adding_cost():#to add up all the expenses so that we can calculate net income
    
    
    x = sum(value for key, value in operating_cost.items())#didnt know u can do this to this day 
    y = sum(value for key, value in employee_salary.items())#to add the values in each list
    z = sum(value for key, value in product_cost.items())
        
    a = x + y + z
           
    print(f"Overall Cost of Expenses: ${a}")
    
    return a
                
      
while 1:
    print("") 
    random_inspirational_words()
    
#asking a question #I used "str" to solve constant error for when you put random things in the input
    question = str(input("""
Options:
1. Print Current List's 
2. Add Items to lists's 
3. Remove Items from List's
4. Pre-Tax Net Income
5. Exit
"""))
    
    if question == "1":#simply printing 
        
        print("Operating Cost")
        OC.print_things()
        print("")
        
        print("Employee's Salaries") 
        ES.print_things()
        print("")
        
        print("Product Cost's")
        PC.print_things()
        print("")
        
        e = adding_cost()
        
        
    elif question == "2":#adding items from lists
        
        while True:
            add_question = str(input("""
What list do you want to Add To?

1. Operating Cost
2. Employee's Salaries
3. Product Cost's
4. Exit
"""))#since we are working with many lists
            
            if add_question == "1":
                OC.adding_things()
               
                
            elif add_question == "2":
                ES.adding_things()
                
                
            elif add_question == "3":
                PC.adding_things()
                
                
            elif add_question == "4":
                break
            
            else:
                print("ONLY USE NUMBERS ABOVE")#This is for when the anwser is given a integer but not 1,2,3,4
                
          
                    
        
    
    elif question == "3":#removing items from lists
        
        while True:
            remove_question = str(input("""
What list do you want to Remove From?

1. Operating Cost
2. Employee's Salaries
3. Product Cost's
4. Exit
"""))#since we are working with many lists
            
            if remove_question == "1":
                OC.remove_things()
               
                
            elif remove_question == "2":
                ES.remove_things()
                
                
            elif remove_question == "3":
                PC.remove_things()
                
                
            elif remove_question == "4":
                break
            
            else:
                print("ONLY USE NUMBERS ABOVE")#This is for when the anwser is given a integer but not 1,2,3,4
            
            
        
    
    elif question == "4":#net income 
        
        while True: 
        
            try:
            
                d = float(input("What was the business Total Revenue?(Only numbers) "))#gets the revenue
                e = adding_cost()
                        
                net_income = d - e
                
                print(f"Net Income is ${net_income}")#after subtracting it prints
                break
                
            except:
                print("ONLY NUMBERS")#fool proof so float numbers are inputed
                continue 
                
            
                       
    
    elif question == "5":
        time.sleep(3)
        break
    
    else:
        print("ONLY USE NUMBERS: 1,2,3,4,5")
        continue
    
#1. what is the diffirence between OOP and Procedural Coding?
#	the main diffirencce 



