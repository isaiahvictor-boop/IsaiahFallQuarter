# import the Flasl library into this file
from flask import Flask

# Create a new Flask app named  "app"
app = Flask(__name__)

# Create a home pae for our flask app (website)
@app.route('/') # the route for the home page
def Index():
    return "Hello World"

if __name__ == '__main__':
    app.run(debug = True)