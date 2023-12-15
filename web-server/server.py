from flask import Flask,request,render_template , make_response,Response
import json
import pickle
import os


current_dir = os.getcwd()
current_dir = os.path.basename(current_dir)

model_file_path = "diabetes-model.pkl"
if current_dir != "web-server":
    model_file_path = "web-server/" + model_file_path

print("model_file_path: ", model_file_path)
loaded_model = pickle.load(open(model_file_path,"rb"))

app = Flask(__name__)
@app.route('/predict',methods =['POST'])
def predict():
    try:
        posted_message = request.data
        json_input = json.loads(posted_message)
        inputs = json_input['features']
        results = loaded_model.predict(inputs).tolist()
        # print(results, type(results))
        return json.dumps(results), 200
    except Exception as es:
        print(es)
        return json.dumps({
            "application error message": "Invalid input",
            "system error message": str(es)
        }), 400

if __name__ =='__main__':
    app.run(host = "0.0.0.0",port="8080")
