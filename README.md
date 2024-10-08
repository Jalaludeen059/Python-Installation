﻿# Python-Installation
Here’s a simplified, plain-English version for your `README.md` file that explains how to set up and run the Flask web application:

---

# Simple Flask Web Application

This guide will walk you through setting up and running a basic Flask web application that displays personalized greetings.

## Step 1: Install Python
- If you don’t have Python installed on your computer, download and install it from the official Python website [here](https://www.python.org/downloads/).
- During installation, be sure to select the option to **Add Python to PATH**.

## Step 2: Create a Project Folder
- Create a new folder on your computer where you will store the Flask application. For example, create a folder named `flask_app`:
  ```
  C:\Users\<YourName>\flask_app
  ```

## Step 3: Create the Application File
- Inside the `flask_app` folder, create a new file named `app.py`. This file will contain the code for the Flask application.

## Step 4: Install Flask
- Open a terminal (or command prompt) and navigate to the `flask_app` folder:
  ```bash
  cd C:\Users\<YourName>\flask_app
  ```
- Install Flask using `pip` by running the following command:
  ```bash
  pip install Flask
  ```

## Step 5: Write the Flask Application
- Open the `app.py` file in your text editor and copy the following code into it:

  ```python
  from flask import Flask

  app = Flask(__name__)

  @app.route('/')
  def index():
      return '<h1>Jalal</h1>'

  @app.route('/about')
  def about():
      return '<h1>About Jalal</h1>'

  @app.route('/users/<name>')
  def user(name):
      return '<h1>Hello, {}!</h1>'.format(name.upper())

  if __name__ == '__main__':
      app.run(debug=True)
  ```

- This code defines three routes:
  - `/`: Displays "Jalal".
  - `/about`: Displays "About Jalal".
  - `/users/<name>`: Displays a personalized greeting, where `<name>` is any name entered in the URL.

## Step 6: Run the Application
- To start the application, run the following command in the terminal:
  ```bash
  python app.py
  ```
- You should see output that looks like this:
  ```bash
  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
  ```

## Step 7: Access the Application in Your Browser
- Open a web browser and visit the following URLs:
  - [http://127.0.0.1:5000/](http://127.0.0.1:5000/): This will display "Jalal".
  - [http://127.0.0.1:5000/about](http://127.0.0.1:5000/about): This will display "About Jalal".
  - [http://127.0.0.1:5000/users/YourName](http://127.0.0.1:5000/users/YourName): Replace `YourName` with any name, and it will display "Hello, YOURNAME!".

## Conclusion
You have successfully created and run a simple Flask web application! Now you can modify and expand this app to fit your needs.

