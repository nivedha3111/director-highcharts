from flask import Flask, render_template, jsonify
import random
import json

app = Flask(__name__)
PORT = 3500

FILEPATH = "data.json"



@app.route("/", methods=["GET", "POST"])
def startpy():

    result = {

        "Greetings": "Tactlabs welcomes you"
    }

    return render_template("index.html")




@app.route("/data", methods=["GET"])
def read_json():

    data = None
    with open(FILEPATH) as json_file:
        data = json.load(json_file)

    
    movie_list = ['Pizza', 'Jigarthanda', 'Bench Talkies', 'Iraivi', 'Mercury', 'Petta',
                  'Putham Pudhu Kaalai', 'Jagame Thandhiram', 'Chiyaan 60']

    rate_list = [6.2, 8.3, 5.7, 8.0, 6.2, 7.3, 6.9,
                 'yet to be released', 'yet to be released']

    result_dict = {
        'movie': movie_list,
        'local_data': data,
        'movie_names': 'Movie names',
        'title': 'Movies directed by Karthik Subbaraj and their IMDb rating ',
        'subtitle': 'Source: https://en.wikipedia.org/wiki/Karthik_Subbaraj',
        'temp_data': rate_list
    }

    return jsonify(result_dict)

    


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=PORT)
