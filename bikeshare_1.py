import time
import pandas as pd
import numpy as np

# create a single dataframe inclusive of the data from the 3 cities
# this will allow an "all cities" analysis.
dfchi = pd.read_csv('chicago.csv')
dfnyc = pd.read_csv('new_york_city.csv')
dfwas = pd.read_csv('washington.csv')

# add city column to each dataframe
dfchi = dfchi.assign(city = 'chicago')
dfnyc = dfnyc.assign(city = 'new york city')
# add city column and missing columns 'Gender' & 'Birth Year' to washington df
dfwas = dfwas.assign(Gender = 'NA', Birth_Year = 'NA', city = 'washington')
# change Birth Year column name in dfwas to 'Birth Year' to ensure consistency
# with the other dataframes.
dfwas = dfwas.rename(columns={'Birth_Year':'Birth Year'})

# join chicago dataframe with nyc dataframe first as they have all the same
# column names
df = pd.concat([dfchi, dfnyc, dfwas], axis = 0)

def get_filters(city, month, day):
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
# get user input for city (chicago, new york city, washington).
    while True:
        city = input("Enter the city (all, chicago, new york city, washington): ")
        if city.lower() not in ('chicago','new york city', 'washington', 'all'):
           print("Not a valid input. Please try again.")
           continue
        # value given is appropriate. exit loop.
        else:
            break
    return city
# get user input for month (all, january, february, ... , june)
    while True:
        month = input("Enter the month (all, january, february,..., june)")
        if month.lower() not in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
# convert the Start Time column to datetime
            df['Start Time'] = pd.to_datetime(df['Start Time'])
# extract month and day of week from Start Time to create new columns
            df['month'] = df['Start Time'].dt.month
            df['day_of_week']=df['Start Time'].dt.weekday_name
            print("Not a valid input. Please try again.")
# value given is appropriate. exit loop.
        else:
            break
    return month
# get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        weekday = input("Enter the specific month (all, january - june): ")
        if weekday.lower() not in ('all','monday','tuesday','wednesday','thursday','friday','saturday'):
           print("Not a valid input. Please try again.")
           continue
    # value given is appropriate. exit loop.
        else:
            break
    return weekday
