function formValidation() {
  var mandatory = document.getElementsByClassName("mandatory");
  var celularRegex = /[0-9]/; // Only Numbers Regex for the Phone input

  for (var i = 0; i < mandatory.length; i++) {
    console.log(mandatory.lenght);
    if (mandatory[i].value == "") {
      alert(
        "Você deve preencher o campo " + mandatory[i].name + " para prosseguir."
      );
      return false;
    } else if (mandatory[i].name == "celular") {
      if (!mandatory[i].value.match(celularRegex)) {
        alert("Somente números no campo " + mandatory[i].name + ".");
        return false;
      } else {
        return;
      }
    }
  }
}

function validatePhoto() {
  var photo = document.getElementsByName("foto");

  // Check if the browser supports the File API
  if (window.File && window.FileReader && window.FileList && window.Blob) {
    var fileSize = photo[0].files[0].size;
  }
  if (fileSize > 1048576) {
    alert("Arquivos maiores de 1MB não são permitidos!");
    return false;
  }
}

function checkboxes() {
  var inputElements = document.querySelectorAll('input[type="checkbox"]');
  for (var i = 0; i < inputElements.length; i++) {
    inputElements[i].onclick = function() {
        verifyCheckboxes();
    }
  }
  verifyCheckboxes();
}

function verifyCheckboxes() {
    var inputElements = document.querySelectorAll('input[type="checkbox"]');
    var contador = 0;
    for (var i = 0; i < inputElements.length; i++) {
      if(inputElements[i].checked == true){
          contador++;
      }
    }
    if(contador == 3) {
        for (var i = 0; i < inputElements.length; i++) {
          if(inputElements[i].checked != true){
              inputElements[i].disabled = true;
          }
        }
    }else{
        for (var i = 0; i < inputElements.length; i++) {
          inputElements[i].disabled = false;
        }
    }
}
