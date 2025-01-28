import os
import flask
import legal 
from flask import Flask, request, render_template


app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')
    
# Add this block to start the Flask app when running locally
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
    # app.run(debug=True)




