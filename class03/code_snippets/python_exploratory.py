####
# Exercise 1
####

# Get to know your data
df.head()

# Have a look at categorical columns, df.Loan_Purpose for instance
print(df.Loan_Purpose.nunique())
print(df.Loan_Purpose.unique())

####
# Exercise 2
####

# Matplotlib is always integrated with pandas, meaning that some visualisations are straightforward
df.Amount_Requested.hist()

####
# Exercise 3
####

# Crossed box plots can be straightforward… with other libraries, such as seaborn. Let's import it!
import seaborn as sns

# link to the seaborn gallery & doc for boxplots
# https://seaborn.pydata.org/examples/horizontal_boxplot.html

# box plots to compare the requested amount based on the Loan_Purpose column
sns.boxplot(x="Amount_Requested", y="Loan_Purpose", data=df,
            whis="range", palette="vlag") 


