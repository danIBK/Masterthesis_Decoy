function validate_quiz(){
    document.getElementById("quiz2").required = true;
    document.getElementById("quiz3").required = true;
    document.getElementById("quiz21").required = true;
    document.getElementById("quiz24").required = true;


    if (parseFloat(document.getElementById('quiz1').value) > 0) {
        document.getElementById('quiz1').oninvalid="this.setCustomValidity('check plz')"
        document.getElementById('quiz1').onchange="this.setCustomValidity('')"
    }
    if (parseFloat(document.getElementById('quiz2').value) > 0) {
        document.getElementById('quiz2').value = 2;
        }
    if (parseFloat(document.getElementById('quiz3').value) > 0) {
        document.getElementById('quiz3').value = 3;
    }
    if (parseFloat(document.getElementById('quiz1').value) > 10000) {
        document.getElementById('quiz3').value = 4;
        }
    }

    function checkForm(form)  {
    if(!form.terms.checked) {
      alert("Please indicate that you accept the Terms and Conditions");
      form.terms.focus();
      return false;
    }
    return true;
}


function validate(){
    	var elements = document.getElementsByName("quiz_vola");
        var statusText = "<br />";

	for (var index=0;index < elements.length;index++){
           statusText += elements[index].value+"-"+elements[index].checked+"<br />";
	}
        document.getElementById("status").innerHTML = statusText;
}
