'''
Welcome to COUNTRY GDP - REGRESSION ANALYSIS
Filedata.py it has three classes - file_data, OLS Model
file_data class has function that pulls data from the csv file
OLS Model class generates the regression
'''
# importing external libraries 
import pandas as pd                     # importing pandas
from statsmodels.api import OLS         # importing statsmodels

# class file_data has one method get_data, it gets data from the CSV file
class file_data:
	def __init__(self, filename, key):              # initializations
		self.fn=filename
		self.key=key
	
	# Function to get data
	def get_data(self,key):                         # get_data method
                X = []
                Y = []
                data2 = pd.read_csv(self.fn, encoding = "ISO-8859-1")
                data1=data2[data2['CID'] == self.key]    # filtering data to specific country code
                Y=data1['GDP']                           # storing GDP in Y
                X=data1[['CON','GOV','CAP','EXP','IMP']] # storing the remaining KPIs in X
                return X,Y                               # returning X and Y

class OLSModel(file_data):                              # Class OLS Model which imports data from class file_data - inheritance - Project Requirement
	def __init__(self, filename, X, Y, key):        # initializations
		file_data.__init__(self, filename, key)
		self.y=Y
		self.x=X
		self.key=key
		
	def olsm(self):                                 # olsm method. returns regression analysis
                model = OLS(self.y, self.x)
                result = model.fit()                    # fitting data to regression co-efficient
                return result                           # returning result

