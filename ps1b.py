# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 12:16:37 2019

@author: Acer
"""
"""
% Inputs Section
  User enters annual salary into annual_salary
  display "Enter your annual Salary:"
  User enters monthly %tage of salary to be saved into portion_saved
  dısplay "Enter the percent of your salary to save, as a decimal:"
  User enters total cost of dream home into total_cost.
  display "Enter the cost of your dream home:​ + total_cost".
  User enters semi annual raıse percentage to be increased every 6 months
  
"""

annual_salary = float(input("Enter Your Annual Salary:"));

portion_saved = float(input("Enter the Percent of your salary to save, as a decimal:"));

total_cost = float(input("Enter the cost of your dream home:"));

semi_annual_raise = float(input("Enter Semi anuual Salary raise, as decimal :"));

"""
% Static variables to be initialized and used in the program.
  define initial down payment for home as down_payment --> 25% of total_cost.
  define current saving as current_saving --> 0
  Define annual return rate on current savings as r --> 4%.
  define tehe number of months are num_months --> 0
"""
down_payment = 0.25 * total_cost;
current_savings = 0;
r = 0.04;
num_months = 0;
"""
% Processing.
  define the amount left after down_payment is removed from total cost as amount_needed --> total_cost - 25% of total_cost.
  define monthly salary as monthly_income --> annual_salary / 12 
  define the monthly returns on current savings as monthly_returns--> current_savings * r /12.
"""
amount_needed = total_cost - (0.25 * total_cost);
monthly_income = annual_salary / 12;
monthly_returns = 0;



"""
  while current_savings is less than or equal to  amount_needed:
	current_savings --> current_savings + portion_saved * monthly_income + monthly_returns.
	monthly returns on current savings gets monthly_returns --> current_savings * r /12.
	İncrement the number of months --> +1
   Afte r every 6 months increase annual salary by semi raıse percentage
"""	
while(current_savings <= down_payment):
    num_months += 1;
    monthly_income = annual_salary / 12;
    current_savings = current_savings + (portion_saved * monthly_income) + monthly_returns;  
    monthly_returns = current_savings * (r  / 12);
    if num_months % 6 == 0:
        annual_salary += semi_annual_raise * annual_salary;
    
   
    
    
"""   
% output
 display "The number of months
"""
print("Number of months :", num_months);