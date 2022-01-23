
function reqListener () {
    
    let data=JSON.parse(this.responseText)
    
    let all_jpg = new RegExp('jpg','i');// 忽略大小寫
    let all_http  = new RegExp('http');
    let http_jpg = ""
    var all_imgs = new Array()
    let all_stitles = new Array()
        for(var i = 0 ; i<=data['result']['results'].length-1;i++){
            let allimg = data['result']['results'][i]['file']
            let  allstitle = data['result']['results'][i]['stitle'];
            for(var j = allimg.match(all_http)['index'] ;j<= allimg.match(all_jpg)['index']+2;j++){
                http_jpg = http_jpg + allimg[j]
            }
        all_imgs.push(http_jpg)
        all_stitles.push(allstitle)
        http_jpg = ""
        allstitle = ""
        
        }

        show_img(0,7);

        function show_img(start_time,end_time){
            let third = document.getElementById("third");
            for(var i = start_time ; i<=end_time;i++){
                let all_div = document.createElement("div");
                all_div.class = "allimg";
                all_div.id = "allimg"+[i];
                third.appendChild(all_div);
            }
            for(var i = start_time ; i<=end_time;i++){
                let get_img = document.getElementById("allimg"+[i])
                let put_p = document.createElement("p");     
                put_p.id = "allimgs"+[i];
                get_img.appendChild(put_p);
                let get_p = document.getElementById('allimgs'+[i]);
                let show_img = document.createElement("img"); 
                show_img.src=all_imgs[i];
                get_p.appendChild(show_img);
            }
            for(var i = start_time ; i<=end_time;i++){
                let all_span = document.createElement("span");
                all_span.id = "all_stitle"+[i];
                let get_img = document.getElementById("allimg"+[i]);
                get_img.appendChild(all_span);
                let get_span = document.getElementById('all_stitle'+[i]);
                let input_stitle = document.createElement("p");    
                input_stitle = document.createTextNode(all_stitles[i]);
                get_span.appendChild(input_stitle);
            }
           
        }
        
        let btn = document.getElementById("btn")
        let start_time = 8
        let end_time = 15
        let click_time = 1
       
        btn.addEventListener("click", function(){
          
            show_img(start_time,end_time);
            end_time = end_time + 8
            start_time = start_time + 8
            click_time = click_time + 1
            if(click_time==6){
                document.getElementById("btn").style.visibility="hidden"
            }
        })
    }

var oReq = new XMLHttpRequest();
oReq.addEventListener("load", reqListener);
var asd = oReq.open("GET", "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json");
oReq.send();



