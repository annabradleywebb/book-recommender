from flask import Flask, request, render_template
from test_make_pred import topic_recommendation, holistic_recommendation

# create a flask object
app = Flask(__name__)

# creates an association between the / page and the entry_page function (defaults to GET)
@app.route('/')
def entry_page():
    return render_template('test_index.html')

# creates an association between the /predict_recipe page and the render_message function
# (includes POST requests which allow users to enter in data via form)
@app.route('/predict_recipe/', methods=['GET', 'POST'])


def render_message():

    # user-entered attributes
    user_isbn = request.form['isbn']

    # error messages to ensure correct units of measure
    # messages = ["Please enter a 0 or a 1."]

    # amounts = []
    # for i, ing in enumerate(attributes):
    #    user_input = request.form[ing]
    #    try:
    #        float_attribute = float(user_input)
    #    except:
    #        return render_template('index.html', message=messages[i])
    #    amounts.append(float_attribute)
    #print(amounts)

    # show user final message
    final_message = topic_recommendation(int(user_isbn))
    array = final_message.split(":")
    message_topics = array[1]
    original_topics = message_topics.split(',')
    message_newbook = str("You may also like:" + array[3])
    message_author = str(array[5]).replace('[', '')
    message_author = str("By" + message_author.replace(']', ''))
    message_newtopics = array[7]
    new_topics = message_newtopics.split(',')

    print(final_message)
    return render_template('test_index.html',
    orig_topic1=str("Main topics in the book you liked:" + original_topics[0] + ','),
    orig_topic2=str(original_topics[1] + ','),
    orig_topic3=original_topics[2],
    message2=message_newbook,
    message3=message_author,
    new_topic1 =str("Its main topics are:" + new_topics[0] + ','),
    new_topic2 = str(new_topics[1] + ','),
    new_topic3 = new_topics[2])

if __name__ == '__main__':
    app.run(debug=True)