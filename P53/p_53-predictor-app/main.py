from flask import Flask, request, render_template
from make_prediction import active_inactive

# create a flask object
app = Flask(__name__)

# creates an association between the / page and the entry_page function (defaults to GET)
@app.route('/')
def entry_page():
    return render_template('index.html')

# creates an association between the /predict_recipe page and the render_message function
# (includes POST requests which allow users to enter in data via form)
@app.route('/predict_recipe/', methods=['GET', 'POST'])
def render_message():

    # user-entered ingredients
    ingredients = ['c59', 'c68', 'c171', 'c1', 'c151', 'c128', 'c39', 'c135', 'c21', 'c160']

    # error messages to ensure correct units of measure

    # hold all amounts as floats
    amounts = []

    # takes user input and ensures it can be turned into a floats
    for i, ing in enumerate(ingredients):
        user_input = request.form[ing]
        amounts.append(user_input)

    # show user final message
    final_message = active_inactive(amounts)
    return render_template('index.html', message=final_message)

if __name__ == '__main__':
    app.run(debug=True)