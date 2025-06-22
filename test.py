import google.generativeai as genai

genai.configure(api_key="AIzaSyDd2WYIKlp4X7-0MHXDYGrL2X-DP8tq6LU")

for model in genai.list_models():
    print(model.name, model.supported_generation_methods)
