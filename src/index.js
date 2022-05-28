var urlbox = document.getElementById("urlbox");
urlbox.focus();

document.getElementById("open_all_btn").addEventListener("click", function(){
    getURLs();
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
function getURLs()
{
    var urls = urlbox.value.split("\n");
    for(i=0; i<urls.length; i++)
    {
        openURL(urls[i]);
    } 
}
function openURL(url){
    //This is the function that opens a URL in a new tab
    chrome.tabs.create({
        active: false,
        url,
    });
}
