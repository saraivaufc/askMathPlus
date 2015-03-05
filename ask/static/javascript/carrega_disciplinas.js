function carrega_disciplinas(){
	$.get("/saida/getDisciplinas/", function(data){
		var disciplinas = JSON.parse(data);
		for(var i=0 ; i< disciplinas.length; i++){
			var semestre = disciplinas[i].fields.semestre;
			var nome = disciplinas[i].fields.nome;
			var html ='<tr class="text-center"><td><input type="radio" name="opcao" id="opcao" value="' + disciplinas[i].pk + '" required></td><td>' + semestre + '</td><td>' + nome + '</td></tr>';
			$(".disciplinas").append(html);
				
		}
	});
}