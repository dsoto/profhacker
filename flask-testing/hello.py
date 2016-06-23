# TODONE: put on button
# TODONE: figure out the devserver thing
# TODONE: learn HTML form elements
# TODONE: route back to the same form, password validation is a good example
# TODONE: create a radio button quiz question and echo answer
# TODO: define quiz data model
# TODO: iterate over quiz data model in template with {{ for }} stuff

from flask import Flask, request, render_template
app = Flask(__name__)

questions = [{'id': 'simple_addition_1',
  'options': [{'correct': False, 'feedback': 'too low', 'text': 3},
   {'correct': True, 'feedback': 'correct', 'text': 4},
   {'correct': False, 'feedback': 'too high', 'text': 5},
   {'correct': False, 'feedback': 'too high', 'text': 6}],
  'prompt': 'What is \\(2^2\\)?'},
 {'id': 'simple_addition_2',
  'options': [{'correct': False, 'feedback': 'too low', 'text': 4},
   {'correct': True, 'feedback': 'correct', 'text': 5},
   {'correct': False, 'feedback': 'too high', 'text': 6},
   {'correct': False, 'feedback': 'too high', 'text': 7}],
  'prompt': 'What is 2 + 3?'}]

@app.route("/", methods=['GET', 'POST'])
def hello():

    if request.method == 'GET':
        return "Hello World!"

    if request.method == 'POST':
        return "You posted something " + request.form.get('field1')

@app.route("/input", methods=['GET', 'POST'])
def input():

    if request.method == 'GET':
        return render_template('form.html',
                            text_response ='text_response',
                            questions = questions)

    if request.method == 'POST':
        return render_template('form.html',
                            text_response=request.form.get('field1'),
                            radio_response=request.form.get('q1'))

if __name__ == "__main__":
    app.run()

# you used this for manual testing
# import requests
# r = requests.post('http://localhost:5000',data={'field1':'one'})
# r.text

# to set up the dev server:
# export FLASK_APP=hello.py
# export FLASK_DEBUG=1
# flask run
