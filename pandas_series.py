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

fruits.value_counts().nlargest(n=1, keep='all') #alternative

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
fruits.str.count('a')

# Output the number of vowels in each and every string value.
# def a fx to count vowels

fruits.str.count('[aieou]') #best option

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

fruits.apply(vowel_count)
fruits.apply(vowel_count2)
import timeit


###### I was curious about the two functions defined above
%%timeit
[fruits.apply(vowel_count2)] 
#141 µs ± 2.78 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

%%timeit
[fruits.apply(vowel_count)]
#148 µs ± 4.01 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

%%timeit
[fruits.str.count('[aieou]')]
#137 µs ± 2.29 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

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


# Exercises Part III
# Use pandas to create a Series named letters from the following string. 
# The easiest way to make this string into a Pandas series is to use list 
# to convert each individual letter into a single string on a basic Python list.


letters =list('hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy')
type(letters)
print(letters)
letters = pd.Series(letters)
type(letters)

# Which letter occurs the most frequently in the letters Series?
letters.mode
letters.value_counts().nlargest(n=1,keep ='all')

# Which letter occurs the Least frequently?
letters.value_counts().nsmallest(n=1,keep ='all')

# How many vowels are in the Series?
letters.apply(vowel_count).sum()

# How many consonants are in the Series?
letters[~letters.isin(['a','e','i','o','u'])].count()

# Create a Series that has all of the same letters but uppercased.
upper_letters=letters.str.upper()
print(upper_letters)

# Create a bar plot of the frequencies of the 6 most commonly occuring 
# letters.
letters.value_counts().nlargest(n=6,keep ='all').plot()
plt.tick_params(axis='x', colors='w')
plt.tick_params(axis='y', colors='w')
plt.xlim(0, 6)
plt.ylim(6, 14)
plt.show()

# Use pandas to create a Series named numbers from the following list:


num_series = pd.Series(['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23'])
# What is the data type of the numbers Series?
print(type(num_series))
print(num_series)
# How many elements are in the number Series?
num_series.count()

# Perform the necessary manipulations by accessing Series attributes 
# and methods to convert the numbers Series to a numeric data type.
def launder_the_cash(money):
    return money.replace('$','').replace(',','')
cash_as_float = num_series.apply(launder_the_cash).astype('float')
print(cash_as_float)

# Run the code to discover the maximum value from the Series.
cash_as_float.max()


# Run the code to discover the minimum value from the Series.
cash_as_float.min()

# What is the range of the values in the Series?
cash_as_float.max()-cash_as_float.min()

# Bin the data into 4 equally sized intervals or bins and output 
# how many values fall into each bin.
pd.cut(cash_as_float,4).value_counts()
# (-4511.11, 1197705.993]       7
# (3592560.778, 4789988.17]     6
# (1197705.993, 2395133.385]    4
# (2395133.385, 3592560.778]    3

# Plot the binned data in a meaningful way. Be sure to include a title 
# and axis labels.
pd.cut(cash_as_float,4).value_counts().plot.bar(rot=0)
font1 = {'family':'serif','color':'white','size':20}
plt.title('Cash Bins',  fontdict= font1)
plt.tick_params(axis='x', colors='w')
plt.tick_params(axis='y', colors='w')
#plt.xlim(0, 6)
# plt.ylim(6, 14)
plt.xlabel('Bins', c='w')
plt.ylabel('Quantity', c='w')
plt.xticks([0,1,2,3],['~$1m', '~$2m', '~$3m', '~$4m'])
plt.show()

# Use pandas to create a Series named exam_scores from the following list:


exam_scores = pd.Series([60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78])
# How many elements are in the exam_scores Series?
exam_scores.size
exam_scores.count()

# Run the code to discover the minimum, the maximum, the mean, 
exam_scores.min()
exam_scores.max()
exam_scores.mean()
# and the median scores for the exam_scores Series.
exam_scores.median()

# Plot the Series in a meaningful way and make sure your chart has a 
# title and axis labels.
exam_scores.plot.hist()
font1 = {'family':'serif','color':'white','size':20}
plt.title('Exam Scores',  fontdict= font1)
plt.tick_params(axis='x', colors='w')
plt.tick_params(axis='y', colors='w')
#plt.xlim(0, 6)
# plt.ylim(6, 14)
plt.xlabel('students', c='w')
plt.ylabel('grades', c='w')
#plt.xticks([0,1,2,3],['~$1m', '~$2m', '~$3m', '~$4m'])
plt.show()
# Write the code necessary to implement a curve for your exam_grades 
# Series and save this as curved_grades. Add the necessary points to 
# the highest grade to make it 100, and add the same number of points 
# to every other score in the Series as well.
scale = 100-exam_scores.max()
curved_grades=exam_scores+scale

# Use a method to convert each of the numeric values in the curved_grades
# Series into a categorical value of letter grades. For example, 
# 86 should be a 'B' and 95 should be an 'A'. Save this as a Series 
# named letter_grades.
def get_letter_grade(grade=90):
    """take in int grade and return letter grade"""
    # check conditions and return once met
    if grade > 88:
        return 'A'
    elif grade > 79:
        return 'B'
    elif grade > 66:
        return 'C'
    elif grade > 59:
        return 'D'
    else:
        return 'F'

letter_grades = curved_grades.apply(get_letter_grade)
print(letter_grades)

# Plot your new categorical letter_grades Series in a meaninful way 
# and include a title and axis labels.

letter_grades.value_counts().plot.bar(rot=0)
font1 = {'family':'serif','color':'white','size':20}
plt.title('Curved Grades',  fontdict= font1)
plt.tick_params(axis='x', colors='w')
plt.tick_params(axis='y', colors='w')
#plt.xlim(0, 6)
# plt.ylim(6, 14)
plt.xlabel('Grades', c='w')
plt.ylabel('Students', c='w')