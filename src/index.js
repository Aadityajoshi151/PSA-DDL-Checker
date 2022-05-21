var urlbox = document.getElementById("urlbox");
urlbox.focus();

document.getElementById("open_all_btn").addEventListener("click", function(){
    alert("Are you sure you want to open all these links?")
})

document.getElementById("clear_btn").addEventListener("click", function(){
    urlbox.value='';
    urlbox.focus();
})

document.getElementById("separator_btn").addEventListener("click", function(){
    urlbox.value+="\n*******************************************************\n"
    urlbox.focus();
})