from flask import Flask


app = Flask(__name__)

@app.route("/",methods=['GET'])
def welcome():
    return 'welcome my website'

@app.route('/index',methods=['GET'])
def index():
    return 'welcome to index page'

if __name__ == "__main__":
    app.run(debug=True)

