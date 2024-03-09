from flask import Flask               #Flask is a library to create API's
from flask import request                                  
                                        #pip install flask
app = Flask(__name__)
                                        #Agar hame ouput dekhna h to ham
                                        #  sabse pahle app tak url copy karenge 
                                        # then :5000 and search to hame hamara o/p dikh jayega 
                                        # Agar hame Hello World1 ko dekhna h to ham app tak copy karenge
                                        #  then :5000/hello_world1 and search 
@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"


@app.route("/hello_world1")
def hello_world1():
    return "<h1>Hello, World1!</h1>"



@app.route("/hello_world2")
def hello_world2():
    return "<h1>Hello, World2!</h1>"


@app.route("/test")
def test():
    a = 5+6
    return "This is my funciton to run app {}".format(a)



#input
@app.route("/test2/test2")            #@app.route ke under hamne path include kiya h /test2/test2 taki ham test2 fun tak pahuch sake 
                                        #Abhi agar hame input lena h to ham url me hi input le lenge app tak url copy karna h then :5000/test2/test2?x=Prince Chouhdury  
def test2():
    data = request.args.get('x')
    return "This is data input from my url {}".format(data)

if __name__=="__main__":
    app.run(host="0.0.0.0")
