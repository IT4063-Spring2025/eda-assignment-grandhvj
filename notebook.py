#!/usr/bin/env python
# coding: utf-8

# # Exploratory Data Analysis - Assignment
# 
# ## 🔍 Overview
# This lab is designed to help you practice exploratory data analysis using Python. You will work with some housing data for the state of California. You will use various data visualization and analysis techniques to gain insights and identify patterns in the data, and clean and preprocess the data to make it more suitable for analysis. The lab is divided into the following sections:
# 
# - Data Loading and Preparation
# - Data Visualization
# - Data Cleaning and Preprocessing (using visualizations)
# 
# ## 🎯 Objectives
# This assignment assess your ability to:
# - Load and pre-process data using `pandas`
# - Clean data and preparing it for analysis
# - Use visualization techniques to explore and understand the data
# - Use visualization techniques to identify patterns and relationships in the data
# - Use visualization to derive insights from the data
# - Apply basic statistical analysis to derive insights from the data
# - Communicate your findings through clear and effective data visualizations and summaries

# #### Package Imports
# We will keep coming back to this cell to add "import" statements, and configure libraries as we need

# In[1]:


# Common imports
import numpy as np
import pandas as pd
from scipy.stats import trim_mean

# To plot figures
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib as mpl
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

# Install seaborn if not already installed
get_ipython().run_line_magic('pip', 'install seaborn')
import seaborn as sns

# Configure pandas to display 500 rows; otherwise it will truncate the output
pd.set_option('display.max_rows', 500)
mpl.rc('axes', labelsize=14)
mpl.rc('xtick', labelsize=12)
mpl.rc('ytick', labelsize=12)
plt.style.use("bmh")


# ## Housing Data in California

# ### Task 1:  Load the dataset
# The dataset is available in the `data/housing.csv` file. Check the file to determine the delimiter and/or the appropriate pandas method to use to load the data.
# 
# Make sure you name the variable `housing` and that you use the appropriate pandas method to load the data.

# In[2]:


# 💻 Import the dataset in the project (data/housing.csv) into a dataframe called (housing)
import pandas as pd

# Load the dataset
housing = pd.read_csv("data/housing.csv")

# Display the first few rows
housing.head()


# ### Task 2: Confirm the data was loaded correctly

# #### 2.1: Get the first 6 records of the dataset

# In[3]:


# 💻 Get the first 6 records of the dataframe
housing.head(6)


# #### 2.2: Get the last 7 records of the dataset

# In[4]:


# 💻 Get the last 7 records of the dataframe
housing.tail(7)


# #### 2.3: Get a random sample of 10 records

# In[5]:


# 💻 Get a random 10 records of the dataframe
housing.sample(10)


# #### 2.4: Get information about the dataset, including the number of rows, number of columns, column names, and data types of each column

# In[6]:


# 💻 Show information about the different data columns (columns, data types, ...etc.)
housing.info()


# > 🚩 This is a good point to commit your code to your repository.

# ### Task 3: Understand the data types
# For each of the 10 columns, Identify the data type: (Numerical-Continuous, Numerical-Discrete, Categorical-Ordinal, Categorical-nominal )
# 
# <details>
# <summary>Click here for the data type diagram</summary>
# 
#   ![Data types](https://miro.medium.com/max/1400/1*kySPZcf83qLOuaqB1vJxlg.jpeg)
# </details>
Longitude:          💻:
Latitude:           💻:
Housing Median Age: 💻:
Total Rooms:        💻:
Total Bedrooms:     💻:
Population:         💻:
Households:         💻:
Median Income:      💻:
Median House Value: 💻:
Ocean Proximity:    💻:
# > 🚩 This is a good point to commit your code to your repository.

# ### Task 4: Understand the data
# #### 4.1: Get the summary statistics for the numerical columns

# In[7]:


# 💻 Show the descriptive statistics information about the columns in the data frame
housing.describe()


# #### 4.2: For the categorical columns, get the frequency counts for each category
# 
# <details>
#   <summary>🦉 Hints</summary>
# 
#   - Use the `value_counts()` method on the categorical columns
# </details>

# In[8]:


# 💻 Show the frequency of the values in the ocean_proximity column
housing['ocean_proximity'].value_counts()


# > 🚩 This is a good point to commit your code to your repository.

# ### Task 5: Visualize the data

# #### 5.1: Visualize the distribution of the numerical columns
# In a single figure, plot the histograms for all the numerical columns. Use a bin size of 50 for the histograms

# In[9]:


# 💻 Plot a histogram of all the data features( with a bin size of 50)
import matplotlib.pyplot as plt
housing.hist(bins=50, figsize=(12, 8))
plt.tight_layout()  # Adjust layout to prevent overlap
plt.show()


# #### 5.2: Visualize the distribution of only one column
# Plot the histogram for the `median_income` column. Use a bin size of 50 for the histogram

# In[10]:


# 💻 plot a histogram of only the median_income
housing['median_income'].hist(bins=50, figsize=(8, 5))
plt.xlabel('Median Income')
plt.ylabel('Count')
plt.title('Distribution of Median Income')
plt.show()


# > 🚩 This is a good point to commit your code to your repository.

# #### 5.3: Visualize the location of the houses using a scatter plot
# In a single figure, plot a scatter plot of the `longitude` and `latitude` columns. 
# 
# 
# Try this twice, once setting the `alpha` parameter to set the transparency of the points to 0.1, and once without setting the `alpha` parameter.

# In[11]:


# 💻 scatter plat without alpha
housing.plot(kind='scatter', x='longitude', y='latitude', figsize=(10, 6))
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('House Locations')
plt.show()


# In[12]:


# 💻 scatter plat with alpha
housing.plot(kind='scatter', x='longitude', y='latitude', alpha=0.1, figsize=(10, 6))
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('House Locations (with Transparency)')
plt.show()


# > 🚩 This is a good point to commit your code to your repository.

# 💯✨ For 3 Extra Credit points; Use the Plotly express to plot the scatter plot on a map of california
# 
# (📜 Check out the examples on their docs)[https://plotly.com/python/scatter-plots-on-maps/]

# In[16]:


# 💻💯✨ Plot the data on a map of California

import pandas as pd
import plotly.express as px

# Load housing data from a CSV file
housing_data = pd.read_csv('data/housing.csv')  


# Set up the map with Plotly Express using the housing data
fig = px.scatter_mapbox(housing_data, lat="latitude", lon="longitude",  
                         size="population", color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=5,
                         mapbox_style="carto-positron",
                         title="Scatter Plot on California Map")

# Show the plot
fig.show()


# > 🚩 This is a good point to commit your code to your repository.

# ### Task 6: Explore the data and find correlations

# #### 6.1: Generate a correlation matrix for the numerical columns

# In[14]:


# 💻 Get the correlation matrix of the housing data, excluding the 'ocean_proximity' column
corr_matrix = housing.drop('ocean_proximity', axis=1).corr()
print(corr_matrix)



# #### 6.2: Get the Correlation data fro the `median_house_age` column
# sort the results in descending order

# In[16]:


# 💻 Get the correlation data for just the housing_median_age
corr_house_age = corr_matrix['housing_median_age'].sort_values(ascending=False)
print(corr_house_age)


# #### 6.2: Visualize the correlation matrix using a heatmap
# - use the coolwarm color map
# - show the numbers on the heatmap
# 

# In[17]:


# 💻 Plot the correlation matrix as a heatmap
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Correlation Matrix Heatmap")
plt.show()


# #### 6.3: Visualize the correlations between some of the features using a scatter matrix
# - Plot a scatter matrix for the `total_rooms`, `median_house_age`, `median_income`, and `median_house_value` columns

# In[19]:


# 💻 using Pandas Scatter Matrix Plotting, Plot the scatter matrix for (median_house_value, median_income, total_rooms, housing_median_age)
from pandas.plotting import scatter_matrix

scatter_features = ["median_house_value", "median_income", "total_rooms", "housing_median_age"]
scatter_matrix(housing[scatter_features], figsize=(10, 8), alpha=0.2)
plt.show()


# #### 6.4: Visualize the correlations between 2 features using a scatter plot
# - use an `alpha` value of 0.1

# In[20]:


# 💻 Plot the scatter plot for just (median_income and median_house_value)
housing.plot(kind="scatter", x="median_income", y="median_house_value",
             alpha=0.1, figsize=(8, 6))
plt.xlabel("Median Income")
plt.ylabel("Median House Value")
plt.title("Correlation between Median Income and House Value")
plt.show()


# #### 6.5: ❓ What do you notice about the chart? what could that mean?
# What could the lines of values at the top of the chart mean here?

# The chart likely represents a correlation matrix of the housing dataset, where the values indicate the strength and direction of the relationships between different features. The lines of values at the top of the chart are likely the names of the features being compared, helping to identify which variables are correlated with each other. High positive or negative values suggest strong relationships between features, such as a high correlation between sqft_living and price, which might indicate that larger houses tend to have higher prices. Weak correlations, close to 0, suggest no significant linear relationship between those features. The diagonal values are always 1, as each feature is perfectly correlated with itself.

# > 🚩 This is a good point to commit your code to your repository.

# ### Task 7: Data Cleaning - Duplicate Data

# #### 7.1: Find duplicate data

# In[23]:


# 💻 Identify the duplicate data in the dataset
duplicates = housing[housing.duplicated()]
print(duplicates)


# ### Task 8: Data Cleaning - Missing Data

# #### 8.1: Find missing data

# In[24]:


# 💻 Identify the missing data in the dataset
missing_data = housing.isna().sum()  # or housing.isnull().sum()
print(missing_data)


# #### 8.2: show a sample of 5 records of the rows with missing data
# Notice there are 2 keywords here: `sample` and (rows with missing data)
# 
# <details>
#   <summary>🦉 Hints:</summary>
# 
#   * You'll do pandas filtering here
#   * You'll need to use the `isna()` or `isnull()` method on the 1 feature with missing data. to find the rows with missing data
#   * you'll need to use the `sample()` method to get a sample of 5 records of the results
# </details>

# In[25]:


# 💻 use Pandas Filtering to show all the records with missing `total_bedrooms` field
missing_total_bedrooms = housing[housing['total_bedrooms'].isna()]
sample_missing = missing_total_bedrooms.sample(5)
print(sample_missing)


# #### 8.3: Calculate the central tendency values of the missing data feature
# * Calculate the mean, median, trimmed mean

# In[27]:


# 💻 get the mean, median and trimmed mean of the total_bedrooms column
import numpy as np
from scipy import stats

# Calculate mean
total_bedrooms_mean = housing['total_bedrooms'].mean()

# Calculate median
total_bedrooms_median = housing['total_bedrooms'].median()

# Calculate trimmed mean (remove top and bottom 10% of data)
total_bedrooms_trimmed_mean = stats.trim_mean(housing['total_bedrooms'].dropna(), proportiontocut=0.1)

print(f"Median: {total_bedrooms_median}")
print(f"Mean: {total_bedrooms_mean}")
print(f"Trimmed Mean: {total_bedrooms_trimmed_mean}")


# #### 8.4: Visualize the distribution of the missing data feature
# * Plot a histogram of the missing data feature (total_bedrooms)

# In[28]:


# 💻 Plot the histogram of the total_bedrooms column
import matplotlib.pyplot as plt

housing['total_bedrooms'].hist(bins=50, edgecolor='black')
plt.title('Distribution of Total Bedrooms')
plt.xlabel('Total Bedrooms')
plt.ylabel('Frequency')
plt.show()


# #### 8.5: Choose one of the central tendency values and use it to fill in the missing data
# * Justify your choice
# * Don't use the `inplace` parameter, instead, create a new dataframe with the updated values. (this is a bit challenging)
# * show the first 5 records of the new dataframe to confirm we got the full dataframe
# 
# [📜 You should find a good example here](https://www.sharpsightlabs.com/blog/pandas-fillna/#example-2)

# In[29]:


# 💻 Fill the missing values in the total_bedrooms column with an appropriate value, then show the first 5 records of the new dataframe
housing_filled = housing.copy()  # Create a new dataframe
housing_filled['total_bedrooms'].fillna(total_bedrooms_median, inplace=False)

# Show the first 5 records of the new dataframe
print(housing_filled.head())


# ❓ Why did you choose this value?

# We are filling with the median because it's less affected by outliers compared to the mean, making it a more robust choice for missing data imputation in a column like total_bedrooms.

# #### 8.6: Confirm that there are no more missing values in the new dataframe
# * make sure the dataframe contains all features, not just the `total_bedrooms` feature

# In[30]:


# 💻 Confirm the new dataframe has no missing values
missing_data_after_imputation = housing_filled.isna().sum()
print(missing_data_after_imputation)


# #### 8.7: Dropping the missing data
# assume we didn't want to impute the missing data, and instead, we wanted to drop the rows with missing data.
# * don't use the `inplace` parameter, instead, create a new dataframe with the updated values.

# In[31]:


# 💻 drop the missing rows of the total_bedroom and save it to a new dataframe
housing_dropped = housing.dropna(subset=['total_bedrooms'])

# Show the first 5 records of the new dataframe
print(housing_dropped.head())


# #### 8.8: Confirm that there are no more missing values in the new dataframe
# * make sure the dataframe contains all features, not just the `total_bedrooms` feature

# In[34]:


# 💻 Confirm the new dataframe has no missing values
missing_data_after_dropping = housing_dropped.isna().sum()
print(missing_data_after_dropping)


# > 🚩 This is a good point to commit your code to your repository.

# ## Wrap up
# Remember to update the self reflection and self evaluations on the `README` file.

# Make sure you run the following cell; this converts this Jupyter notebook to a Python script. and will make the process of reviewing your code on GitHub easier

# In[37]:


# 🦉: The following command converts this Jupyter notebook to a Python script.
get_ipython().system('jupyter nbconvert --to python notebook.ipynb')


# > 🚩 **Make sure** you save the notebook and make one final commit here
