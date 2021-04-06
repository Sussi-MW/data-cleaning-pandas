Goal:

The goal of this project is to combine everything you have learned about data wrangling, cleaning, and manipulation with Pandas. I also define some functions along the project, starting with one messy data set Shark Attack. I use data wrangling skills to clean it up, prepare it to be analyzed, and then export it as a clean CSV data file. 

Procedure:

In short, we proceed as follows:

Hypothesis:
1. The white shark is the terrible bad guy.
Variables: 'Species' and 'Fatal (Y/N)'

2. During the nighttime, sharks tend to be more fatal.
Variables: 'Time' and 'Fatal (Y/N)'

3. Most shark attacks happen in US
Variables: 'Country' 

Data cleaning:
Subset with the variables for the analysis of hypothesis 1
Remove null values
Function to group values ​​in 'Species'
Function to identify the missing_values ​​of the column 'Fatal (Y / N)'
Create new column to filter missing_values ​​as True
Export dataset 1

Subset with the variables for the analysis of hypothesis 2
Remove null values
Function to group values ​​in 'Time'
Create new column to indicate the result of new_values_time
Function to identify the missing_values ​​of the column 'Fatal (Y / N)'
Export dataset 2


Subset with the variables for the analysis of hypothesis 3
Remove null values
Display unique values ​​for 'Country'
Function to replace string in cells
Function to eliminate rows whose variables are not countries
Function to add column with the value_count of 'Country'
Export dataset 3
