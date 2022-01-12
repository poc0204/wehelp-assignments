
function reqListener () {
    
    var ob=JSON.parse(this.responseText)
    
    var jpg1 = new RegExp('jpg','i');// 忽略大小寫
    var http1  = new RegExp('http');
    var qq = ""
    var allimgs = new Array()
    var allstitles = new Array()
        for(var i = 0 ; i<=ob['result']['results'].length-1;i++){
        var allimg = ob['result']['results'][i]['file']
        var  allstitle = ob['result']['results'][i]['stitle'];
        for(var j = allimg.match(http1)['index'] ;j<= allimg.match(jpg1)['index']+2;j++){
            qq = qq + allimg[j]
             

        }
        allimgs.push(qq)
        allstitles.push(allstitle)
        qq = ""
        allstitle = ""
        
        }
        for(var i = 0 ; i<=7;i++){
            var bigImg = document.createElement("img");    
            bigImg.src=allimgs[i];
            var myp = document.getElementById('allimgss'+[i]); //获得dom对象
            myp.appendChild(bigImg);   
        }
        for(var i = 0 ; i<=7;i++){
            var bigp = document.createElement("p");    
            bigp =  document.createTextNode(allstitles[i]);
            var pp = document.getElementById('allstitles'+[i]); //获得dom对象
            pp.appendChild(bigp);
            
        }
    }

var oReq = new XMLHttpRequest();
oReq.addEventListener("load", reqListener);
var asd = oReq.open("GET", "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json");
oReq.send();



