let str=document.getElementsByClassName("star")
let rt=document.getElementById("rate")

function st(n){
    clr();
    for(let i=0; i<n; i++){
        if(n==1){
            cls="one"
        }
        else if(n==2){
            cls="two"
        }
        else if(n==3){
            cls="three"
        }
        else if(n==4){
            cls="four"
        }
        else if(n==5){
            cls="five"
        }
        str[i].className="star "+cls;
    }
    rt.innerHTML="Rating:"+n+"/5";
    rtt=document.getElementById("ratees").value=n;
}
function clr(){
    let i=0;
    while(i<5){
        str[i].className="star";
        i++;
    }
}