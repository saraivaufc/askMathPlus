/* MathJax */
MathJax.Hub.Config({
tex2jax: { inlineMath: [['$','$'], ] }
});

var Preview = {
delay: 150,        // delay after keystroke before updating

preview: null,     // filled in by Init below
buffer: null,      // filled in by Init below

timeout: null,     // store setTimout id
mjRunning: false,  // true when MathJax is processing
oldText: null,     // used to check if an update is needed

Init: function () {
	this.preview = document.getElementById("MathPreview");
	this.buffer = document.getElementById("MathBuffer");
},

SwapBuffers: function () {
		var buffer = this.preview, preview = this.buffer;
		this.buffer = buffer; 
		this.preview = preview;
		buffer.style.visibility = "hidden"; 
		buffer.style.position = "absolute";
		preview.style.position = "";
		preview.style.visibility = "";
},
Update: function () {
	if (this.timeout) {clearTimeout(this.timeout)}
	this.timeout = setTimeout(this.callback,this.delay);
},
CreatePreview: function () {
	Preview.timeout = null;
	if (this.mjRunning) return;
	var text = document.getElementById("latex_formula").value;
	if (text === this.oldtext) return;
	this.buffer.innerHTML = this.oldtext = text;
	this.mjRunning = true;
	MathJax.Hub.Queue(
			["Typeset",MathJax.Hub,this.buffer],
			["PreviewDone",this]
	);
},
PreviewDone: function () {
	this.mjRunning = false;
	this.SwapBuffers();
}};
Preview.callback = MathJax.Callback(["CreatePreview",Preview]);
Preview.callback.autoReset = true;  // make sure it can run more than once	


Init(); var a=new EqTextArea(''); a.addExportArea('eqcoderaw','htmledit'); EqEditor.init('1438691334', a,true); EqEditor.ExportButton.add(a, 'copybutton', EqnExport,'htmledit'); EqEditor.load(''); EqEditor.setAdvert();


