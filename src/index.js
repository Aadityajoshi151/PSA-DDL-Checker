var urlbox = document.getElementById("urlbox");
urlbox.focus();

document.getElementById("open_all_btn").addEventListener("click", function(){
    getUrls();
})

document.getElementById("clear_btn").addEventListener("click", function(){
    urlbox.value='';
    urlbox.focus();
})

document.getElementById("separator_btn").addEventListener("click", function(){
    urlbox.value+="\n*******************************************************\n"
    urlbox.focus();
})

hoster_btns = document.getElementsByClassName("btn-warning")
for(i=0; i<hoster_btns.length;i++)
{
    hoster_btns[i].addEventListener("click",function(){
        alert(this.innerHTML);
    })
}
function getUrls()
{
    var urls = urlbox.value.split("\n");
    for(i=0; i<urls.length; i++)
    {     
        window.open(urls[i], '_wnd' + i);
    }
    

    
}
