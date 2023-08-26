# load data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from dfply import *

# LOAD DATA

# detect files in data folder and read it

df = pd.read_csv('data/Wroclaw, Poland.csv')

# remove NaN columns
df = df.dropna(axis=1, how='all')

# create automatic report

# drop columns that have one value
for col in df.columns:
    if len(df[col].unique()) == 1:
        df.drop(col, inplace=True, axis=1)

# subset data

# room_type = Private room
private_room = df >> mask(X.room_type == 'Private room')
private_room

# room_type = Entire home/apt
entire_home = df >> mask(X.room_type == 'Entire home/apt')
entire_home

# review_count = 0
no_reviews = df >> mask(X.review_count == 0)
no_reviews

# review_count > 0
with_reviews = df >> mask(X.review_count > 0)

# show all columns
pd.set_option('display.max_columns', None)


# Standardize the 'total_price' column
total_price_mean = with_reviews['total_price'].mean()
total_price_std = with_reviews['total_price'].std()
with_reviews['standardized_price'] = (
    with_reviews['total_price'] - total_price_mean) / total_price_std
# absolute value
with_reviews['standardized_price'] = with_reviews['standardized_price'].abs()


# Replace NaN values in 'avg_rating' with a default opacity value
default_opacity = 0.5  # Choose a default opacity value (between 0 and 1)
with_reviews['avg_rating'] = with_reviews['avg_rating'].fillna(default_opacity)

# standardize review_count
review_count_mean = with_reviews['review_count'].mean()
review_count_std = with_reviews['review_count'].std()
with_reviews['standardized_review_count'] = (
    with_reviews['review_count'] - review_count_mean) / review_count_std
