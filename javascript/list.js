function showPost() {
  $.ajax({
    type: "GET",
    url: "/fanclub/list",
    data: {},
    success: function (response) {
      let posts = response["all_posts"];
      for (let i = 0; i < posts.length; i++) {
        let name = posts[i]["name"];
        let comment = posts[i]["comment"];
        let temp_html = `<tr>
                        <td >${name}</td>
                        <td >${comment}</td>
                        <td><input class="delete-button" onclick="deletePost('${name}')" type="button" value="삭제"></td>
                        </tr>`;
        $("#posts-box").append(temp_html);
      }
    },
  });
}
showPost()