from flask import Flask, request, jsonify, render_template
from transformers import PegasusTokenizer, PegasusForConditionalGeneration, TFPegasusForConditionalGeneration

model_name = "human-centered-summarization/financial-summarization-pegasus"
tokenizer = PegasusTokenizer.from_pretrained(model_name)
model = PegasusForConditionalGeneration.from_pretrained(model_name)


app = Flask(__name__)

@app.route('/')
def home():
    return 1

@app.route('/get_message')
def get_message():
    text = request.form['text']
    input_ids = tokenizer(text, return_tensors="pt").input_ids
    output = model.generate(
    input_ids, 
    max_length=32, 
    num_beams=5, 
    early_stopping=True
    )
    result = tokenizer.decode(output[0], skip_special_tokens=True)
    return result

if __name__ == '__main__':
    app.run(debug=True,use_reloader=False,host='0.0.0.0',port=5001)
