import pandas as pd
import numpy as np
import matplotlib

'''
**************READING FILES**************
'''
# Numpy
data = np.genfromtxt('myfile.csv', delimiter=',')  # Read csv
# Pandas
df = pd.read_csv(r'my_file.csv')  # Read csv
df.to_excel('Abc.xlsx', sheet_name='sheet1')  # Read excel


'''
**************WRITING FILES**************
'''
# Numpy
np.save('fname', data)
# Pandas
df.to_csv('Newfile.csv')                        # Write new csv
df.to_excel('Abc.xlsx', sheet_name='sheet2')    # Write new csv


'''
**************STATISTICAL METHODS**************
'''
# Numpy
data.sum()          # Array-wise sum
data.min()          # Array-wise min value
data.max()          # Array-wise max value
data.cumsum(axis=1)  # Cumulative sum of the elements
data.mean()         # Mean
data.median()       # Median
data.corrcof()      # Correlation coefficient
np.std(data)        # Standard deviation

# Pandas
df.describe()       # Returns a quick stats
df.cov()            # Returns co-variance between suitable columns
df.corr()           # Returns co-relation between suitable columns

'''
**************VALUE INFORMATION**************
'''
# Numpy
data.shape          # Returns array shape
data.ndim           # Dimensions of the array
data.dtype()        # data type of the array

# Pandas
df['column1'].unique()  # Returns unique values
df.head()               # Shows top n records
df.tail()               # Shows nottom n records
df.columns              # Return columns names

'''
**************DATA MANIPULATION**************
'''
transposed_data = np.transpose(data)    # Permute array dimension
data.ravel()                            # flatten the array
data.reshape(3, 2)                       # Reshapes does not change data
