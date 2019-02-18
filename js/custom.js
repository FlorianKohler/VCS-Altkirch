

$(document).ready(function(){

	$('ul.dropdown').superfish({
		autoArrows: true,
		animation: {height:'show'}
	});

});

function openCity(evt, cityName) {
    // Declare all variables
    var i, tabcontent, tablinks;

    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(cityName).style.display = "block";
    evt.currentTarget.className += " active";
}




function toggle(sender, target) {
  var ele = document.getElementById(target);
  var text = sender;
  if (ele.style.display == "block") {
    ele.style.display = "none";
    text.innerHTML = "&#x25BA; " + target + " : Lire le résumé";
  } else {
    ele.style.display = "block";
    text.innerHTML = "&#x25BC; " + target + " : Masquer le résumé";
  }
}
