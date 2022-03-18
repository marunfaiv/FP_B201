function getTime(){
    var today = new Date();
    var time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();

    document.getElementById("currentTime").value = time;
}
getTime()