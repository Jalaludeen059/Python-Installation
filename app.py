from flask import Flask
# Import the Flask class from the 'flask' module to create a web application.

app = Flask(__name__)
# Create an instance of the Flask class. This will act as the app object for our web application.

@app.route('/')
# Define the route for the home page ('/'). When someone visits this URL, the function below will be called.

def index():
    return '<h1>Jalal</h1>'
    # This function will return a simple HTML heading when the home page is accessed.

@app.route('/about')
# Define the route for the '/about' page. When someone visits '/about', the function below will run.

def about():
    return '<h1>About Jalal</h1>'
    # This function will return a different HTML heading specifically for the 'About' page.

@app.route('/users/<name>')
# Define a dynamic route. The part '<name>' captures a variable from the URL. If a user visits '/users/John', 'John' will be passed into the function.

def user(name):
    return '<h1>Hello, {}!</h1>'.format(name.upper())
    # This function takes the name passed from the URL, converts it to uppercase, and returns a personalized greeting.

if __name__ == '__main__':
    app.run(debug=True)
    # This ensures the application runs only if this script is executed directly. The 'debug=True' option provides more detailed error messages for debugging purposes.
