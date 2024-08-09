from flask import Flask, request, jsonify, render_template
import gzip, pickle, pickletools
import pandas as pd
from my_funcs import preprocess
import os

app = Flask(__name__)
filepath = r"titanic_model.pkl"
with gzip.open(filepath, 'rb') as f:
    p = pickle.Unpickler(f)
    model = p.load()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    df = pd.DataFrame([data])
    print(df.head())
    df = preprocess(df)
    predictions = model.predict(df)
    output = predictions[0]
    return jsonify({'survived?:': str(output)})

# if __name__ == "__main__":
#     app.run(debug=True)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)
