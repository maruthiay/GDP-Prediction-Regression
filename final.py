'''
Welcome to COUNTRY GDP - REGRESSION ANALYSIS
The project details are given in intro method
'''
# Importing custom libraries being used in our project - Project Requirement
from intro import *             # importing intro.py it has the introductions, code generation for IDs of Country and plot functions of the data 
from filedata import *
'''importing filedata.py it has three classes - file_data, OLS Model
file_data class has function that pulls data from the csv file
OLS Model class generates the regression
'''

# method final that runs in loop!
def final():
    filename = 'eggs3.csv'                                          # declaring the filename to be reused at different places
    intro()                                                         # intro function imported from intro.py , basically gives a description of what our project does.
    get_code(filename)                                              # get_code function imported from intro.py , it prints the list of countries with their ID (or code) using which the user inputs country number 
    key=int(input("\n Please select a Country of your choice:"))       # taking code from the user, it selects the country for which we are going to produce the plot and do regression analysis
    if key in range(1,212):                                         # decision making statement as part of project requirement, checks if the entered country code exists
        fd=file_data(filename,key)                                  # file data class produces data for the 5 KPIs
        X,Y = fd.get_data(key)                                      # X is a combined array of the 5 KPIs and Y is GDP
        om=OLSModel(filename,X, Y, key)                             # initiating OLSModel class
        res=om.olsm()                                               # olsm method on OLSModel class derives the regression
        print(res.summary())                                        # printing the summary of regression on screen
        plotlib(filename,key)                                       # plotlib function is in intro.py, it plots the KPIs and GDP to Year and saves the plot as a pdf - writing data to file requirement.
    else:
        print(" \n Wrong country code , Check again")                  # Just an else statement if the user enters a country code that does not exist




r = 'Y'                                                             # declaring r for iterating the process!- project requirement
while (r == 'Y' or r =='y'):                                        # loop statements - project requirement to run the project in a loop till the user wants to exit
    final()
    r=input("\n Press y if you want to generate report for another country: ")

    
    
