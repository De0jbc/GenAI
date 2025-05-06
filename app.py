from flask import Flask, render_template, request

from tripcrew import TripCrew
from dotenv import load_dotenv
import markdown
import os
import litellm

load_dotenv()
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result=""
    if request.method == "POST":
        location = request.form["location"]
        cities = request.form["cities"]
        date_range = request.form["date_range"]
        interests = request.form["interest"]
        trip_crew = TripCrew(location, cities, date_range, interests)
        result = trip_crew.run()
        result = str(result)
        #result=markdown.markdown(result)
        try:
            result = markdown.markdown(result)
           # print(result)
        except Exception as e:
            print("⚠️ Error:", e)        
        #resultado = f"Hola {nombre}, tienes {edad} años."
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
