function register(){
    window.location.href='register.html'
}


let objUsers = [
    {
        username:"kim",
        password:"1234"
    },
    {
        username:"park",
        password:"12345"
    },
    {
        username:"lee",
        password:"123456"
    }
]

function login(){
    let userId = document.getElementById("userId").value
    let userPW = document.getElementById("userPW").value
    for(i = 0; i <objUsers.length; i++){
        if(userId == objUsers[i].username && userPW == objUsers[i].password){
            alert('환영합니다 ' + userId +'님');
            window.location.href='register.html'
        }
    }alert("아이디나 비밀번호를 확인하세요") 
    
    
        

}

