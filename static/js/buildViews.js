function buildTable(jsonData) {
    for(var i in jsonData.data)
    {
        var dayData = jsonData.data[i];
        var day = dayData.day
        var dvalue = dayData.dvalue;
        if(dvalue == 1)
        {
            document.getElementById(day).className = "Green"
        }
        else if (dvalue == 2)
        {
            document.getElementById(day).className = "Orange"
        }
        else if (dvalue == 3)
        {
            document.getElementById(day).className = "Red"
        }
    }
}