# This is a calculator to figure out the cost of rent per month/year per person
#
# Author: Logan Gremler 12/13/2015

# Determine the cost of everything:
rent = input("What is the monthly rent? ")
utilities = input("What is the estimated utility cost? ")
insurance = input("What are monthly insurance fees? ")
people = input("How many people are there? ")
app_fee = input("How much is the application fee? ")

# Figure out the monthly/yearly costs:
subtotal = rent + utilities
monthly_cost = subtotal / people + insurance #Insurance needs paid monthly
yearly_cost = monthly_cost * 12 + app_fee #The app fee only needs paid once
insurance_cost = insurance * 12

# Figure out the price difference of living in towers:
towers_yearly_cost = 4093
towers_comparison = yearly_cost - towers_yearly_cost

# Figure out the price difference of living in an on-campus apartment:
freddy_yearly_cost = 5496
freddy_comparison = yearly_cost - freddy_yearly_cost

# Relay the final results to the user:
print "The overall monthly cost is: " ,subtotal #Rent + Utilities
print "The cost per person each month is: " ,monthly_cost #Rent + Utilities + Insurance
print "The cost per person each year is: " ,yearly_cost #Rent + Utilities + Insurance + Application Fee
print "The yearly insurance cost is: " ,insurance_cost #Insurance For the Year
print "The apartment is $" +str(towers_comparison), "more expensive than towers" #Apartment Final - Towers Final
print "The apartment is $" +str(freddy_comparison), "more expensive than Freddy Court" #Apartment Final - Freddy Final

