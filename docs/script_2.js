function validateForm() {
   
    var inputs = document.querySelectorAll('input[type="radio"]');
    var cont_aprovado = 0;
    var cont_cancelado = 0;
    var has_alerted = false;
    console.log(inputs);

    for(var i = 0; i < inputs.length; i++)
    {
        if(inputs[i].checked == true && inputs[i].className == "aprovado") {
            cont_aprovado++;
        }
        else if(inputs[i].checked == true && inputs[i].className == "cancelado") {
            cont_cancelado++;
        }
          
    }
    if (cont_aprovado+cont_cancelado<80)
    {
        event.preventDefault();
        alert("Favor preencher todas as opcoes");    
        }
        else if(cont_aprovado < 20)
        {
            event.preventDefault();
            alert("Mínimo de 20 alunos aprovados!");
            return false;
        }
        else if(cont_aprovado > 60)
        {
            event.preventDefault();
            alert("Máximo de 60 alunos aprovados!");
            return false;
    }
    else
    {
        alert("Parabéns ! Formulário enviado com sucesso");
    }
    
}  
