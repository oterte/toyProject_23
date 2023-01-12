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
@app.route('/', methods=['GET'])
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
    name = request.form.get('name')
    comment = request.form.get('comment')



#db 넣기
    if name is not None:
        db.newjeanscomment.insert_one({'name':name, 'comment':comment})
        return render_template('fanclub.html')
    else:
        return render_template('fanclub.html')

#comment delete
@app.route('/fanclub', methods=['GET','POST'])
def delete():
    deleteid = request.form.get('id')
    # deletecomment = request.form.get('comment')


    db.newjeanscomment.delete_one({'name':deleteid})

#signin
@app.route('/signin', methods=['GET','POST'])
def signin():

    #html 받아오기
    userid = request.form.get('id')
    userpw = request.form.get('pw')
    username = request.form.get('name')
    userhp = request.form.get('HP')


#db 집어넣기
    if userid is not None:
        db.newjeans.insert_one({'ID': userid, 'PW': userpw, 'NAME': username, 'HP': userhp})
        return render_template('signin.html')
    else:
        return render_template('signin.html')




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)

