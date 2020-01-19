

from flask import *  
app = Flask(__name__)  
app.secret_key = "abc"  
     
@app.route('/')  
def home():  
	res = make_response("<h4>session variable is set, <a href='/get'>Get Variable</a></h4>")  
	session['response']='session#1'  
	return res;  
	
	
if __name__ == '__main__':  
    app.run(debug = True, port = '3500')  