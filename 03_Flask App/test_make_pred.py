from Recommender import most_similar, most_similar_meta

# create a function to take in user-entered ISBN and apply the model
def topic_recommendation(isbn, model=most_similar):
    # make a prediction
    recommendation = model(isbn)
    # return a message
    return recommendation

def holistic_recommendation(isbn, meta_model=most_similar_meta):
    # make a prediction
    meta_recommendation = meta_model(isbn)
    # return a message
    return meta_recommendation