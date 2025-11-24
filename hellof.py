from flask import Flask, render_template

app = Flask(__name__)


#creat index page
@app.route('/')

def index():
	#first_name = 'James'
	#favorite_pizza = ['Pepperoni', 'Cheese', 'Sausage', 'Meat Lovers']
	#return render_template('index.html', f_name = first_name, f_pizza = favorite_pizza)


# create about page
@app.route('/about')
def about():
	return render_template('about.html')