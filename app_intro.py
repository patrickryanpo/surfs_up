# Import Flask dependency
from flask import Flask

# Create a new FLask app instance. "Instance" is a general term in 
#programming to refer to a singular version of something. The ff code creates
#a new Flask instance: 
app = Flask(__name__) # name variable denotes the name of the current function. 
# __ before and after are called magic methods

# Create out Flask routes
# We need to define the starting point, also known as the root. 
@app.route('/') # / means that we want to put our data at the root of our routes

# Create a function called hello_world()
def hello_world():
    return 'Hello World'
    # Environment variables are essentially dynamic variables in your computer. 
    #They are used to modify the way certain aspect of the computer operates. 
    #export FLASK_APP=app.py
    # run our flask app
#flask run 