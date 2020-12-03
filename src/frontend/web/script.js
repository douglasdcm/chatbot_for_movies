function enviar_mensagem() {
	var campo_mensagem = document.getElementById('campo_mensagem').value;
	
	if (campo_mensagem === "") {
		alert("Fill the message, please!.");
	} else {
		document.getElementById("mensagem").innerHTML = campo_mensagem;
	}	
}
