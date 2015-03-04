function validaAdd(opcao){
	if (opcao == 1){

	}else if(opcao == 2){

	}else if(opcao == 3){
		var item_correto = $("#id_item_correto").val();
		item = null;
		if(item_correto == 1){
			item = $("#id_item_a");
		}else if (item_correto == 2){
			item = $("#id_item_b");
		}else if (item_correto == 3){
			item = $("#id_item_c");
		}else if (item_correto == 4){
			item = $("#id_item_d");
		}else if (item_correto == 5){
			item = $("#id_item_e");
		}
		try{
			if (item.val() == ''){
				alert("Item Correto está vazio!!!");
				return false;
			}
		}catch(e){
			console.log(e);
		}

		var itens = 0;
		if($("#id_item_a").val() != ''){
			itens+=1;
		}
		if($("#id_item_b").val() != ''){
			itens+=1;
		}
		if($("#id_item_c").val() != ''){
			itens+=1;
		}
		if($("#id_item_d").val() != ''){
			itens+=1;
		}
		if($("#id_item_e").val() != ''){
			itens+=1;
		}
		if(itens == 0){
			alert("Toda Pergunta precisa ter pelo menos 1 Item!!!");
			return false;
		}
	}
	return true;
}