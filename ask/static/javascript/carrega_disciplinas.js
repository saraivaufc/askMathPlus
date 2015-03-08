function carrega_disciplinas(){
	$.get("/saida/getDisciplinas/", function(data){
		var disciplinas = JSON.parse(data);
		for(var i=0 ; i< disciplinas.length; i++){
			var semestre = disciplinas[i].fields.semestre;
			var nome = disciplinas[i].fields.nome;
			var html ='<tr class="text-center"><td class="col-md-1"><input type="radio" name="opcao" id="opcao" value="' + disciplinas[i].pk + '" required></td><td class="col-md-12">' + nome + '</td></tr>';
			$(".disciplinas").append(html);
				
		}
	});
}