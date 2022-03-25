function getTime(){
    var today = new Date();
    var time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();

    document.getElementById("currentTime").value = time;
}
getTime()

function openTab(evt, tabName){
    var tabContent, tablinks;
    tabContent = document.getElementsByClassName("tabcontent");
    for(var i = 0; i < tabContent.length; i++)
    {
        tabContent[i].style.display = "none";
    }

    tablinks = document.getElementsByClassName("tab_links");
    for(var i = 0; i < tablinks.length; i++)
    {
        tablinks[i].className = tablinks[i].className.replace("active", "");
    }

    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.classNamec += "active";
}
openTab();