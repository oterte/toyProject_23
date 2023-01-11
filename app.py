from flask import *
from pymongo import MongoClient
import certifi
import bcrypt

#mongodb
ca = certifi.where()
client = MongoClient('mongodb+srv://oterte:kim018@cluster0.cwfwiwz.mongodb.net/?retryWrites=true&w=majority',tlsCAFile=ca)
db = client.dbsparta

#server
app = Flask(__name__)

#secret key
app.secret_key = 'super secret key'

#index
@app.route('/')
def home():
    return render_template('login.html')

#login
@app.route('/login', methods=['GET','POST'])
def login():
    #html 받아오기
    userId= request.form['id']
    userPw= request.form['pw']

    #db검색
    login_id = db.newjenans.find_one({'ID': userId})
    login_pw = db.newjenans.find_one({'PW': userPw})

    #조건문
    if login_id==userId:
        if login_pw==userPw:
            return render_template('fanclub.html')
    else:
        return render_template('login.html')

#main
@app.route('/fanclub', methods=['GET','POST'])
def mainhome():
    return render_template('fanclub.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)

