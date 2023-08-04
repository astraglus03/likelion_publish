function showOrderInfo() {
    document.getElementById("mainContent").style.display = "none";
    document.getElementById("orderInfo").style.display = "block";
  }
  
  date = new Date();
  year = date.getFullYear();
  month = date.getMonth() + 1;
  day = date.getDate();
  document.getElementById("current_date").innerHTML = year + "." + month + "." + day;
  document.getElementById("current_date2").innerHTML = month + "/" + day;