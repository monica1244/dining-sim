import json
import pandas as pd
#change file location
review_json = open('../../yelp-dataset/yelp_academic_dataset_review.json',encoding="utf8")
# read the first 1000 entries
num_reviews=10000
reviews_list = list()
for i, line in enumerate(review_json):
    if i == num_reviews:
        break
    data = json.loads(line)
    # extract fields
    review_id = data['review_id']
    user_id = data['user_id']
    business_id = data['business_id']
    stars = data['stars']
    text = data['text']
    # add to the data
    reviews_list.append([stars,text])

df_review = pd.DataFrame(reviews_list, columns=['stars','text'])

print(df_review.columns)
print(df_review)

df_review.to_csv("stars_reviews.csv", encoding='utf-8', index = False)