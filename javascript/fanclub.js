function add_comment() {
    let name = $('#floatingInput').val()
    let comment = $('#floatingTextarea').val()
    let temp_html = `<div class="card">
<div class="card-body">
<blockquote class="blockquote mb-0">
    <p>${comment}</p>
    <footer class="blockquote-footer">${name} </footer>
    <button type="button" class="btn btn-dark" onclick="delete_comment()">삭제</button>
</blockquote>

</div>
</div>`
    $('#cardArea').append(temp_html)
}



function delete_comment(){
    alert('삭제하시겠습니까?')
    const div = document.getElementById('cardBox')
    div.remove();

}