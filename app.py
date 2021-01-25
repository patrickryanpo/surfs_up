# Import dependencies datetime, numpy, and pandas

import datetime as dt
import numpy as np
import pandas as pd

# SQLAlchemy dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Import Flask dependency, has to be after SQLAlchemy 
from flask import Flask, jsonify

# Set up out database engine for the Flask application.
engine = create_engine("sqlite:///hawaii.sqlite")

# Reflect the database into our classes
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save our references to each table. 
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session link from Python to our database 
session = Session(engine)

# Next, we need to define our app for our Flask application. 
app = Flask(__name__)
# define the welcome route using the code below:
@app.route("/")
# add the routing information for each of the other routes.
#create a function, and our return statement will have f-strings as reference 
#of the other routes.

#Create a function welcome() with a return statement:

def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!<br/>
    Available Routes:<br/>
    /api/v1.0/precipitation<br/>
    /api/v1.0/stations<br/>
    /api/v1.0/tobs<br/>
    /api/v1.0/temp/start/end
    ''')

# When creating routes, we follow the naming convention /api/v1.0/ followed by the name of the route. This convention signifies that this is version 1 of our application. This line 
#can be updated to support future versions of the app as well.

# Create the precipitation route  for analysis (will occur separately from the welcome route)
@app.route("/api/v1.0/precipitation")

def precipitation():
    # add the line of code that calculates the date one year ago from the most recent date in the database
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    # write a query to get the date and precipitation for the prev year
    precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >=prev_year).all()
    #Create a dictionary with the date as the key and precipitation as the value
    # We will use "jsonify" on our dictionary. Jsonify() converts the dict to a JSON file.
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

# Create the stations route 
@app.route("/api/v1.0/stations")
def stations():
    # Create a query that will allow us to get all of the stations in our Database
    results = session.query(Station.station).all()
    # Unraveling our results into a one-dimensional array. 
    # We will use the function np.ravel() with results as our parameter
    stations = list(np.ravel(results))
    # to return our list as json, we need to add stations=stations
    return jsonify(stations=stations)

# Create the tobs route
@app.route("/api/v1.0/tobs")
# def temp_monthly():
#     # Calculate the date one year ago from the last date in the database.
#     prev_year = dt.date(2017, 8, 23) - dt.dt.timedelta(days=365)
#     # Query the primary station for all temperature observations
#     results = session.query(Measurement.tobs).\
#         filter(Measurement.station == 'USC00519281').\
#         filter(Measurement.date >= prev_year).all()
#     # Jsonify the list and return our results into a one-dimensional array and convert into list
#     temps = list(np.ravel(results))
#     return jsonify(temps=temps)
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)
    
# Create the route for start
@app.route("/api/v1.0/temp/<start>")
# Start and End
@app.route("/api/v1.0/temp/<start>/<end>")

# Create a function called stats(), we need to add parameters to our stats function
def stats(start=None, end=None):
    #Create a query to select the minimum, average, max temp from SQLite
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    
    # Create an if-not statement to determine start and end date. Query out database using the list then
    # unravel the results into a one-dimensional array and convert to a list

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).\
            filter(Measurement.date <= end).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)