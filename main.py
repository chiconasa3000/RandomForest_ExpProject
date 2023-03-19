from flask import Flask, request, render_template
import pickle
import numpy as np
import os
# declare a flask app
app = Flask(__name__)

#predict function when you get all data
def value_predictor(to_predict_list):
    print(to_predict_list)
    to_predict = np.array(to_predict_list).reshape(1,12)
    loaded_model = pickle.load(open("model.pkl","rb"))
    result = loaded_model.predict(to_predict)
    return result[0]

# main function he
@app.route("/",methods=["GET","POST"])
def index():
    return render_template("index.html")

@app.route("/result", methods=["GET","POST"])
def result():
    # if a form is submitted
    if request.method == "POST":

        # get values from the form
        to_predict_list = request.form.to_dict() 
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(int, to_predict_list))
        result = value_predictor(to_predict_list)

        if int(result) == 1:
            prediction = "more than 50k"
        else:
            prediction = "less than 50k"
    else:
        prediction = ""

    return render_template("result.html", prediction=prediction)

# running the app
if __name__ == "__main__":
    app.run(debug=True, port=os.getenv("PORT", default=5000))
