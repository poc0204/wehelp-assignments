
function select_click(){
  let username = document.getElementById("username");
  
    fetch(`http://127.0.0.1:3000/api/members?username=${username.value}`, {method: 'get'})
    .then(response =>{
      return  response.json()
   })
   .then( data =>{
      console.log(data['data'] )
        let showname = document.getElementById("showname")
        if ( data['data'] != null){
          showname.innerText = data['data']['name'];
        } 
        else {
          showname.innerText = "查無此人";
        }
       
       
  })

}

function update_click(){
  let updataname = document.getElementById("updataname");
  let url = `http://127.0.0.1:3000/api/member`
  let headers = { "Content-Type": "application/json"}
  let data = {"name":updataname.value}
  fetch(url, {method: 'post' ,  headers: headers , body: JSON.stringify(data)})
  .then(response =>{
    return response.json()
 })
 .then( data =>{

  if (data['ok'] == true){
    showupdate.innerText = "更新成功";
  }
  else {
    showupdate.innerText = "更新失敗";
  }
})

}
