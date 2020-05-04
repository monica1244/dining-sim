import json

import ast
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


business_file = '/kaggle/input/yelp-dataset/yelp_academic_dataset_business.json'
review_file = '/kaggle/input/yelp-dataset/yelp_academic_dataset_review.json'
user_file = '/kaggle/input/yelp-dataset/yelp_academic_dataset_user.json'
tip_file = '/kaggle/input/yelp-dataset/yelp_academic_dataset_tip.json'
checkin_file = '/kaggle/input/yelp-dataset/yelp_academic_dataset_checkin.json'

# BUSINESS.JSON
business_data = []
print('Reading business.json')
with open(business_file) as f:
    for line in f:
        business_data.append(json.loads(line))
business_df = pd.DataFrame.from_dict(business_data)

business_restaurant_df = business_df.loc[business_df['categories'].str.contains("Restaurants", na=False)]

# now that sample file is made, get list of business id's from it
# convert into a dict with values as keys for fast searching
print('Getting business_ids')
business_ids = pd.Series(business_restaurant_df['business_id'].index.values, index=business_restaurant_df['business_id']).to_dict()


#REVIEW.JSON
review_data_1 = []
review_data_2 = []
review_data_3 = []
review_data_4 = []
review_data_5 = []

print('Reading review.json') 
with open(review_file) as f:
    for line in f:
        newline = ast.literal_eval(line)  # read the line (str) as a dict
        if newline['stars']==1.0 and newline['business_id'] in business_ids:
            with open("reviews_1.txt", "a") as myfile:
                myfile.write(newline['text'])
        elif newline['stars']==2.0 and newline['business_id'] in business_ids:
            with open("reviews_2.txt", "a") as myfile:
                myfile.write(newline['text'])
        elif  newline['stars']==3.0 and newline['business_id'] in business_ids:
            with open("reviews_3.txt", "a") as myfile:
                myfile.write(newline['text'])
        elif  newline['stars']==4.0 and newline['business_id'] in business_ids:
            with open("reviews_4.txt", "a") as myfile:
                myfile.write(newline['text'])
        elif  newline['stars']==5.0 and newline['business_id'] in business_ids:
            with open("reviews_5.txt", "a") as myfile:
                myfile.write(newline['text'])
        
        


