from flask import Flask, render_template, request
import tensorflow as tf
from tensorflow.keras import models, layers
import numpy as np
from cv2 import *
import shutil

app = Flask(__name__)

class_names= ['Early Blight','Late Blight','Septoria Leaf Spot','No Disease :)','Yellow Leaf Curl Virus']

model = models.load_model('trained_model_new.h5')
def predict(model, img):
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)

    predictions = model.predict(img_array)

    predicted_class = class_names[np.argmax(predictions[0])]
    confidence = round(100 * (np.max(predictions[0])), 2)
    return predicted_class, confidence


@app.route('/')
def index():
	return render_template("index.html")


@app.route("/prediction", methods=["POST"])
def prediction():

	img = request.files['img']
	img.save("img.jpg")
	img.save("static/img.jpg")

	shutil.copyfile('img.jpg','static/img.jpg')

	image = cv2.imread("img.jpg")
	image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	image = cv2.resize(image, (256,256))
	predicted_class, confidence = predict(model, image)

	return render_template("prediction.html", data=predicted_class, conf=confidence)

if __name__ == "__main__":
	app.run(debug=True)
