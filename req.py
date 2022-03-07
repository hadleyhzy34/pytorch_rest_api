import requests

resp = requests.post("http://localhost:5000/predict",
                     files={"file": open('/home/hadley/development/pytorch-flask-api/cat_1.jpg','rb')})

print(resp.text)

# import ipdb;ipdb.set_trace()
# print('test')
