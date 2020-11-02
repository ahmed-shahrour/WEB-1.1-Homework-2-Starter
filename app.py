from flask import Flask, request, render_template
import random

app = Flask(__name__)


def sort_letters(message):
    """A helper method to sort the characters of a string in alphabetical order
    and return the new string."""
    return ''.join(sorted(list(message)))


@app.route('/')
def homepage():
    """A homepage with handy links for your convenience."""
    return render_template('home.html')


@app.route('/froyo')
def choose_froyo():
    """Shows a form to collect the user's Fro-Yo order."""
    return """
    <form action="/froyo_results" method="GET">
        <label for="flavor">What is your favorite Fro-Yo flavor?:</label>
        <input id="flavor" type="text" name="flavor"><br/>
        <label for="toppings">Choose your toppings:</label>
        <input id="toppings" type="text" name="toppings"><br/>
        <input type="submit" value="Submit!">
    </form>
    """


@app.route('/froyo_results')
def show_froyo_results():
    users_froyo_flavor = request.args.get('flavor')
    users_toppings = request.args.get('toppings')
    return f'You ordered {users_froyo_flavor} flavored Fro-Yo with toppings {users_toppings}!'


@app.route('/favorites')
def favorites():
    """Shows the user a form to choose their favorite color, animal, and city."""
    return """
    <form action="/favorites_results" method="GET">
        <label for="color">What is your favorite color?:</label>
        <input id="color" type="text" name="color"><br/>
        <label for="animal">What is your favorite animal?:</label>
        <input id="animal" type="text" name="animal"><br/>
        <label for="city">What is your favorite city?:</label>
        <input id="city" type="text" name="city"><br/>
        <input type="submit" value="Submit!">
    </form>
    """


@app.route('/favorites_results')
def favorites_results():
    """Shows the user a nice message using their form results."""
    users_color = request.args.get('color')
    users_animal = request.args.get('animal')
    users_city = request.args.get('city')
    return f"Wow, I didn't know {users_color} {users_animal}s lived in {users_city}!"


@app.route('/secret_message')
def secret_message():
    """Shows the user a form to collect a secret message. Sends the result via
    the POST method to keep it a secret!"""
    return """
    <form action="/message_results" method="POST">
          <label for="message"></label>
          <input id="message" name="message" type="text"><br/>
          <input type="submit" value="Submit!">
    </form>
    """


@app.route('/message_results', methods=['POST'])
def message_results():
    """Shows the user their message, with the letters in sorted order."""
    users_secret_message = request.form.get('message')
    secret_message_sorted = sort_letters(users_secret_message)

    return f"Here's your secret message!\n {secret_message_sorted}"


@app.route('/calculator')
def calculator():
    """Shows the user a form to enter 2 numbers and an operation."""
    return """
    <form action="/calculator_results" method="GET">
        Please enter 2 numbers and select an operator.<br/><br/>
        <input type="number" name="operand1">
        <select name="operation">
            <option value="add">+</option>
            <option value="subtract">-</option>
            <option value="multiply">*</option>
            <option value="divide">/</option>
        </select>
        <input type="number" name="operand2">
        <input type="submit" value="Submit!">
    </form>
    """


@app.route('/calculator_results')
def calculator_results():
    """Shows the user the result of their calculation."""
    operand1 = int(request.args.get('operand1'))
    operation = request.args.get('operation')
    operand2 = int(request.args.get('operand2'))

    result = None

    if operation == 'add':
        result = operand1 + operand2
    elif operation == 'subtract':
        result = operand1 - operand2
    elif operation == 'multiply':
        result = operand1 * operand2
    elif operation == 'divide':
        result = operand1 / operand2

    return f"You chose to {operation} {operand1} and {operand2}. Your result is: {result}"


# List of compliments to be used in the `compliments_results` route (feel free
# to add your own!)
# https://systemagicmotives.com/positive-adjectives.htm
list_of_compliments = [
    'awesome',
    'beatific',
    'blithesome',
    'conscientious',
    'coruscant',
    'erudite',
    'exquisite',
    'fabulous',
    'fantastic',
    'gorgeous',
    'indubitable',
    'ineffable',
    'magnificent',
    'outstanding',
    'propitioius',
    'remarkable',
    'spectacular',
    'splendiferous',
    'stupendous',
    'super',
    'upbeat',
    'wondrous',
    'zoetic'
]


@app.route('/compliments')
def compliments():
    """Shows the user a form to get compliments."""
    return render_template('compliments_form.html')


@app.route('/compliments_results')
def compliments_results():
    """Show the user some compliments."""
    context = {
        # TODO: Enter your context variables here.
    }

    return render_template('compliments_results.html', **context)


if __name__ == '__main__':
    app.run()
