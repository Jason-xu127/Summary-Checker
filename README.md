# Summary-Checker
## Model Selection
Since our checkpoint models are too big to be uploaded to Github, we have provided a lite verision here using Chat-GPT API and Pre-trained model provided by Huggingface. If you are interested in our Reject-SUMM and FactGraph model, please dowload them with this link https://drive.google.com/drive/folders/1-DvDybsqmGFZcdjmnAi0IA19wmHRg6aj?usp=share_link.

## Installation

Install the dependencies and start the server.

```sh
pip install flask
pip install pytorch
pip install transformers
```

Run the server application and language model application.
```sh
python3 app_debug.py
python3 summary_generate.py
```

Then, open your browser and enter http://127.0.0.1:5000 to use the application.
