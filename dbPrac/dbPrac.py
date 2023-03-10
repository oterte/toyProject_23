from pymongo import MongoClient
client = MongoClient('mongodb+srv://oterte:kim018@cluster0.cwfwiwz.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta




# pymongo로 DB 조작하기
# db.users.insert_one({'name' : 'bobby','age' : 7}) # 데이터 넣기
# db.users.insert_one({'name' : 'cassie','age' : 27})
# db.users.insert_one({'name' : 'kim','age' : 17})

# 모든 데이터 뽑아보기
all_users = list(db.users.find({},{'_id':False}))

print(all_users[0])         # 0번째 결과값을 보기
print(all_users[0]['name']) # 0번째 결과값의 'name'을 보기

for user in all_users:      # 반복문을 돌며 모든 결과값을 보기
    print(user)

# 특정 결과 값 뽑기
user = db.users.find_one({'name':'bobby'})
print(user)

# 수정하기
db.users.update_one({'name':'bobby'},{'$set':{'age':28}})

user = db.users.find_one({'name':'bobby'})
print(user)

# 삭제하기
# db.users.delete_one({'name':'bobby'})
#
# user = db.users.find_one({'name':'bobby'})
# print(user)