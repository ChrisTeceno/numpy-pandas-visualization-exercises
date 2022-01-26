# Exercises Part I
# Make a file named pandas_series.py or pandas_series.ipynb for the 
# following exercises.
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np

# Use pandas to create a Series named fruits from the following list:


fruits = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", 
"honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", 
"mango", "blueberry", "blackberry", "gooseberry", "papaya"])

# Use Series attributes and methods to explore your fruits Series.

# 1. Determine the number of elements in fruits.
print(len(fruits)) # 17

# Output only the index from fruits.
print(fruits.index)

# Output only the values from fruits.
print(fruits.values)

# Confirm the data type of the values in fruits.
print(fruits) # dtype object
print(type(fruits[0])) # 'str'
print(type(fruits.values)) #np.array

# Output only the first five values from fruits. Output the last three values. 
# Output two random values from fruits.
print(fruits.head())
print(fruits.tail(3))
print(fruits.sample(2))

# Run the .describe() on fruits to see what information it returns when 
# called on a Series with string values.
fruits.describe()

# Run the code necessary to produce only the unique string values from fruits.
fruits.unique()

# Determine how many times each unique string value occurs in fruits.
fruits.value_counts()

# Determine the string value that occurs most frequently in fruits.
fruits.mode() #mode

a=fruits.value_counts() # order by unique values and their counts
a.head(1) #first result of series sorted by count

#make a list in case there is a tie
most_freq = list( a.where(a == a.max()).dropna().index ) 
print(most_freq)
fruits.value_counts().nlargest(n=1, keep='all') 

# Determine the string value that occurs least frequently in fruits.
fruits.value_counts().nsmallest(n=1, keep='all') 

a=fruits.value_counts()
a[a==a.min()]
a.tail(1) #gives lowest, but does not account to ties
a[a==a.min()] #returns a series where count == lowest count
type(a[a==a.min()]) #prove its a panda series
a[a==a.min()].index #show it as indexes
#make a list of least frequents
least_freq = list( a[a==a.min()].index )
print(least_freq) # list of least common fruits




# Exercises Part II
# Explore more attributes and methods while you continue to work with the 
# fruits Series.

# Capitalize all the string values in fruits.
fruits.str.upper()

# Count the letter "a" in all the string values (use string vectorization).
fruits.str.count('a').sum()

# Output the number of vowels in each and every string value.
# def a fx to count vowels

def vowel_count(some_string):
    """function to count values"""
    vowel_count=0
    for vowel in 'aieouAEIOU':
        vowel_count += some_string.count(vowel)
    return vowel_count

# def a fx to count vowels using str.lower()
def vowel_count2(some_string):
    """function to count values"""
    vowel_count=0
    for vowel in 'aieou':
        vowel_count += some_string.lower().count(vowel)
    return vowel_count

fruits.apply(vowel_count).sum()
fruits.apply(vowel_count2).sum()
import timeit


###### I was curious about the two functions defined above
%%timeit
[fruits.apply(vowel_count2).sum()] 
#2 20 µs ± 23.6 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

%%timeit
{fruits.apply(vowel_count).sum()}
# 227 µs ± 8.79 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)



# Write the code to get the longest string value from fruits.
print(max(fruits, key=len))

# Write the code to get the string values with 5 or more letters in the name.
print(fruits[fruits.str.len()>4])

# Use the .apply method with a lambda function to find the fruit(s) 
# containing the letter "o" two or more times.
print(fruits[fruits.str.count('o')>1])

two_os = list(filter(lambda n: (n.count('o')>1), fruits))
print(two_os)
# Write the code to get only the string values containing the substring 
# "berry".
print(fruits[fruits.str.count('berry')>0])

has_berry = list(filter(lambda n: (n.count('berry')>0), fruits))
print(has_berry)

# Write the code to get only the string values containing the substring "apple".
print(fruits[fruits.str.count('apple')>0])

has_berry = list(filter(lambda n: (n.count('apple')>0), fruits))
print(has_berry)

# Which string value contains the most vowels?
def vowel_count(some_string):
    vowel_count=0
    for vowel in 'aieouAEIOU':
        vowel_count += some_string.count(vowel)
    return vowel_count
print(max(fruits, key=vowel_count))
