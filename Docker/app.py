from flask import Flask
import os
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Hello, world!"

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=5000)
    
# You can see the results:  192.168.0.127:5000  || localhost:5000 || 127.0.0.0:5000

# create a docker: docker build -t welcome-app .
# to see the docker: docker images
# docker run -p 5000:5000 welcome-app
# docker ps - how many containers:  0.0.0.0:5000->5000 it means its exciting from host port to container port
# docker stop container_id....