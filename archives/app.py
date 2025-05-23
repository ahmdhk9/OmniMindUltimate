from flask import Flask, request, jsonify
from flask_ngrok import run_with_ngrok
import numpy as np
from tensorflow.keras.models import load_model

app = Flask(__name__)
run_with_ngrok(app)

# تحميل النموذج
model = load_model('/content/drive/MyDrive/AI_Universal_Builder/model_lstm_v1.h5')

@app.route("/")
def home():
    return "✅ الخادم الذكي يعمل الآن!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        input_data = request.json["data"]  # مثال: [1, 0, 1]
        if len(input_data) != 3:
            return jsonify({"error": "يرجى إرسال 3 قيم فقط للتحليل"}), 400

        data = np.array(input_data, dtype=np.float32).reshape(1, 1, 3)
        prediction = model.predict(data)[0][0]
        return jsonify({"prediction": float(prediction)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run()
