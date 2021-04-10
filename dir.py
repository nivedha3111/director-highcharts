from flask import Flask, render_template, jsonify
import random
import json

app  = Flask(__name__)


FILEPATH = "data.json"
    
'''
    http://0.0.0.0:3000/

    https://www.youtube.com/watch?v=wgfc07NJskY
'''
@app.route("/", methods=["GET","POST"])
def startpy():

    result = {

        "Greetings" : "Tactlabs welcomes you"
    }

    return render_template("index.html")

'''
    http://0.0.0.0:3000/data

'''
@app.route("/data", methods=["GET"])
def read_json():

    data = None
    with open(FILEPATH) as json_file:
        data = json.load(json_file)

    

    movie_list = ['Pizza', 'Jigarthanda', 'Bench Talkies', 'Iraivi', 'Mercury', 'Petta', 
        'Putham Pudhu Kaalai', 'Jagame Thandhiram', 'Chiyaan 60']

    rate_list = [6.2, 8.3, 5.7, 8.0, 6.2, 7.3, 6.9, 'yet to be released', 'yet to be released']

    result_dict = {
        'months'        : movie_list,
        'local_data'    : data,
        'city'          : 'karthik subbaraj movies',
        'title'         : 'Monthly Average Temperature',
        'subtitle'      : 'Source: WorldClimate.com',
        'temp_data'     : rate_list 
    }

    return jsonify(result_dict)

    # return render_template("index.html", data = data)

if __name__ == "__main__":
    app.run( debug = True, host="0.0.0.0", port = 3500)
    