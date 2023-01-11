from flask import *
from pymongo import MongoClient
import certifi


#mongodb
ca = certifi.where()
client = MongoClient('mongodb+srv://oterte:kim018@cluster0.cwfwiwz.mongodb.net/?retryWrites=true&w=majority',tlsCAFile=ca)
db = client.dbsparta

#server
app = Flask(__name__)

#secret key
app.secret_key = 'super secret key'

#index
@app.route('/', methods=['GET','POST'])
def home():
    return render_template('login.html')

#login
@app.route('/login', methods=['GET','POST'])
def login():
    #html 받아오기
    userid= request.form['id']
    userpw= request.form['pw']

    # db검색
    userdbid = db.newjeans.find_one({'ID':userid})
    userdbpw = db.newjeans.find_one({'PW':userpw})

    #None 막기 조건문
    if userdbid is None:
        return render_template('login.html')
    elif userdbpw is None:
        return render_template('login.html')
    else:
        return redirect('/fanclub')



#main
@app.route('/fanclub', methods=['GET','POST'])
def fanclub():
    return render_template('fanclub.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

