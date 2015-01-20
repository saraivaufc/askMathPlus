{% extends 'admin/gerenciador/opcao/pergunta/list.php' %}

{% block barra-superior %}
	<div class="col-xs-12 col-sm-12  col-md-12">
		<h3 class="text-center">
			Adicionar Nova Pergunta
		</h3>
	</div>
{% endblock %}

{% block opcoes-padrao %}
	<form  action="."  method="POST" >{% csrf_token %}
		<div class="table-responsive">
			<table class="table table-condensed">
				{{ form.as_table }}
				<tr>
					<td>
						<b>Item A:</b>
					</td>
					<td>
						<textarea id="item_a" name="item_a"></textarea>
					</td>
					<td>
						<b>Deficiencia Item A:</b>
					</td>
					<td>
						<textarea id="deficiencia_a" name="deficiencia_a"></textarea>
					</td>
				</tr>
				<tr>
					<td>
						<b>Item B:</b>
					</td>
					<td>
						<textarea id="item_b" name="item_b"></textarea>
					</td>
					<td>
						<b>Deficiencia Item B:</b>
					</td>
					<td>
						<textarea id="deficiencia_b" name="deficiencia_b"></textarea>
					</td>
				</tr>
				<tr>
					<td>
						<b>Item C:</b>
					</td>
					<td>
						<textarea id="item_c" name="item_c"></textarea>
					</td>
					<td>
						<b>Deficiencia Item C:</b>
					</td>
					<td>
						<textarea id="deficiencia_c" name="deficiencia_c"></textarea>
					</td>
				</tr>
				<tr>
					<td>
						<b>Item D:</b>
					</td>
					<td>
						<textarea id="item_d" name="item_d"></textarea>
					</td>
					<td>
						<b>Deficiencia Item d:</b>
					</td>
					<td>
						<textarea id="deficiencia_d" name="deficiencia_d"></textarea>
					</td>
				</tr>
				<tr>
					<td>
						<b>Item E:</b>
					</td>
					<td>
						<textarea id="item_e" name="item_e"></textarea>
					</td>
					<td>
						<b>Deficiencia Item E:</b>
					</td>
					<td>
						<textarea id="deficiencia_e" name="deficiencia_e"></textarea>
					</td>
				</tr>


				<tr>
					<td>
					 <b>Item Correto:</b>
					</td>
					<td>
						<select id="item_correto" name="item_correto" required>
							<option ></option>
							<option value="a">Item A</option>
							<option value="b">Item B</option>
							<option value="c">Item C</option>
							<option value="d">Item D</option>
							<option value="e">Item E</option>
						</select>
						<br>
						Diga qual desses itens e o correto.
					</td>
				</tr>
				<tr>
					<td>
						<b>Ajuda:</b>
					</td>
					<td>
						<textarea id="ajuda" name="ajuda"></textarea>
					</td>
				</tr>
				{{ ajuda }}
			</table>
		</div>	
		<div class="btn-group">
			<button class="btn btn-primary" onClick="window.location='/gerenciador/list/{{ opcao }}/'; return false; "  type="cancel">Cancelar</button>
			<button type="submit" class="btn btn-primary">Submeter</button>
		</div>
	</form>
{% endblock %}