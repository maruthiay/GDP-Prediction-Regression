'''
Welcome to COUNTRY GDP - REGRESSION ANALYSIS
The project details are given in intro method
'''
# Importing external libraries being used in our project - Project Requirement
import pandas as pd                 # importing pandas
import matplotlib.pyplot as plt     # importing matplotlib to plot

# intro method has print statements that tell about the project
def intro():
    print(" \n ***Welcome to COUNTRY GDP - REGRESSION ANALYSIS*** \n ")
    print(" Below is the List of Countries available in the database ")
    print(" The formula for GDP is: GDP = C + I + G + (Ex - Im),")
    print(" where C equals household consumption, I equals capital investment, G equals government spending and (Ex - Im) equals net exports,")
    print(" that is, the value of exports minus imports. Net exports may be negative.\n")
    print(" Choose the appropriate country number and we shall provide you with a detailed analysis and report of that Country")
    print(" Report Contains :")
    print(" 1. Plot of GDP and the other KPI's with respect to Year")
    print(" 2. Regression Analysis and a summary report of GDP \n")

# get_code function reads the file and prints code number and country as a tuple for the user to chose a country and generate the plot and regression
def get_code(fn):
    data2 = pd.read_csv(fn, encoding = "ISO-8859-1")
    d=list(data2['CID'].unique())       # generates unique country codes
    e=list(data2['Country'].unique())   # generates unique country names
    f=list(zip(d,e))                    # creates a tuple of country code and country names and prints it
    print(f)


# plotlib function reads the file and helps create a plot of the 5 KPIs and GDP vs Year
def plotlib(fn,key):
    data2 = pd.read_csv(fn, encoding = "ISO-8859-1")        # reading the file
    data1=data2[data2['CID'] == key]                        # filtering the file to capture only specific country
    ID = data1['CID']                                       # getting the filtered country code                  
    cty=data1['Country'].unique()                           # getting country name
    gdp = data1['GDP']                                      # gdp stores GDP of the country
    con = data1['CON']                                      # con stores Consumption of the country
    cap = data1['CAP']                                      # cap is Capital Investment
    exp = data1['EXP']                                      # exp is Exports
    imp = data1['IMP']                                      # imp is Imports of the Country
    gov = data1['GOV']                                      # gov stores Government Spending of the Country
    y =data1['Year']                                        # y stores Year values
    plt.figure(1)
    plt.ylabel('All KPIs')                  # Y axis label
    plt.xlabel('Year')                      # X axis label
    plt.title(cty)                          # Title of the plot
    plt.plot(y,gdp, color = 'red', label = 'GDP')       # plotting gdp
    plt.plot(y,con, color = 'blue', label = 'CON')      # plotting consumption
    plt.plot(y,cap, color = 'yellow', label = 'CAP')    # plotting capital investment
    plt.plot(y,exp, color = 'cyan', label = 'EXP')      # plotting exports
    plt.plot(y,imp, color = 'magenta', label = 'IMP')   # plotting imports
    plt.plot(y,gov, color = 'black', label = 'GOV')     # plotting government spending
    plt.legend()
    print(" The generated plot that is displayed is also stored in the path the project is running!")
    plt.savefig(str(cty)+".pdf", format='pdf')          # Storing the plot as a pdf - Project Requirement
    plt.show()                                          # Displaying the plot too!

