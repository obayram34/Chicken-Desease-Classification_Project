from flask import Flask, request, jsonify, render_template 
import os
from Flask_cors import CORS, cross_origin
from CnnClassifier.utils.common import decodeImage
from cnnClassifier.pipeline.prediction import PredictionPipeline


os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_us.UTF-8')


app= Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        self.filename= "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)


@app.route("/", methods= ['GET'])
@cross_origin()
def home():
    return render_template('index.html')



@app.route("/", methods= ['GET', 'POST'])
@cross_origin()
def trainRoute():
    os.system("python main.py")
    return "Training done succesfully !"



@app.route("/", methods= ['POST'])
@cross_origin()
def predictionRoute():
    image= request.json(['image'])
    decodeImage(image, clApp.filename)
    result= clApp.classifier.predict()
    return jsonify(result)



if __name__ == "__main__":
    clApp= ClientApp()
    app.run(host= '0.0.0.0', port=8080)
