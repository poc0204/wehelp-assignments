
function select_click(){
  let username = document.getElementById("username");
  
    fetch(`http://127.0.0.1:3000/api/members?username=${username.value}`, {method: 'get'})
    .then(response =>{
      return  response.json()
   })
   .then( data =>{
        let showname = document.getElementById("showname")
        if ( data['data'] != 'null'){
          showname.innerText = data['data']['name'];
        } 
        else {
          showname.innerText = "查無此人";
        }
       
       
  })


}
