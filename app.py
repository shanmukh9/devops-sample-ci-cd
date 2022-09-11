from flask import Flask
import os
app = Flask(__name__)

<<<<<<< HEAD
@app.route("/")
def hello():
   return "Hello world!!! from Shanmukh"

 
=======

@app.route("/")
def hello():
    return "Hello world!!! from Shanmukh"


>>>>>>> 2b4009cc9831c21e7337eb13559c171298159dff
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
