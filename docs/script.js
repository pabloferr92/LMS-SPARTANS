var form = document.getElementById("formulario");
form.addEventListener("submit", validateForm);

function validateForm(event) {
  //CAMPOS OBRIGATÓRIOS
  var fields = document.getElementsByClassName("obrigatorio");
  //console.log(fields);
  for (var i = 0; i < fields.length; i++) {
    if (fields[i].value == "") {
      event.preventDefault();
      alert("Preenchimento do campo " + fields[i].name + " obrigatório.");
    }
  }

  //VALIDAR SENHA
  var password = document.getElementById("senha").value;
  if (password.search(/[a-zA-Z]/) <= 0 && password.search(/\d/) <= 0) {
    event.preventDefault();
    alert("Senha inválida. Deve possuir ao menos uma letra e um número!");
  }

  //VERIFICAR SE AS SENHAS SÃO IGUAIS
  var confirm_password = document.getElementById("confirma_senha");
  if (confirm_password.value != document.getElementById("senha").value) {
    event.preventDefault();
    alert("Senhas devem ser iguais.");
  }

  //VALIDAÇÃO CPF
  var cpf = document.getElementById("cpf").value;
  var numeros, digitos, soma, i, resultado, digitos_iguais;
  digitos_iguais = 1;
  if (cpf.length < 11) {
    alert("CPF deve ter 11 caracteres!");
    return false;
  }
  for (i = 0; i < cpf.length - 1; i++)
    if (cpf.charAt(i) != cpf.charAt(i + 1)) {
      digitos_iguais = 0;
      break;
    }
  if (!digitos_iguais) {
    numeros = cpf.substring(0, 9);
    digitos = cpf.substring(9);
    soma = 0;
    for (i = 10; i > 1; i--) soma += numeros.charAt(10 - i) * i;
    resultado = soma % 11 < 2 ? 0 : 11 - soma % 11;
    if (resultado != digitos.charAt(0)) { alert("CPF Inválido!"); return false; }
    numeros = cpf.substring(0, 10);
    soma = 0;
    for (i = 11; i > 1; i--) soma += numeros.charAt(11 - i) * i;
    resultado = soma % 11 < 2 ? 0 : 11 - soma % 11;
    if (resultado != digitos.charAt(1)) { alert("CPF Inválido!"); return false; }
    return true;
  } else { alert("CPF Inválido!"); return false; }
}
