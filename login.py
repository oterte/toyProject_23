from flask import *
from pymongo import MongoClient
import certifi

ca = certifi.where()
client = MongoClient('mongodb+srv://oterte:kim018@cluster0.cwfwiwz.mongodb.net/?retryWrites=true&w=majority',tlsCAFile=ca)
db = client.dbsparta

app = Flask(__name__)

# 로그인
@app.route('/', methods = ['GET','POST'])
def login():
    user_id = request.form.get("ID",type=str)
    user_pw = request.form.get("PW",type=str)

    ## *** find_one 시에 아무것도 없을 때의 데이터 형태 알아야함 ***
    user = db.newjeans.find_one( {'ID' : user_id},{'PW' : user_pw})

    if user is None:
        return render_template("login.html")
    else:
        return render_template("fanclub.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)

# 회원가입
@app.route('/register',methods=['POST'])
def register_user():
    name_receive: