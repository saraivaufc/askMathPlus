$(function(){
	/* Google Analytics */
	if (window.location.hostname !== 'localhost' || true ){
		  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
		  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
		  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
		  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');
		
		  ga('create', 'UA-66026376-1', 'auto');
		  ga('send', 'pageview');
	};
})


/* MathJax */
MathJax.Hub.Config({
	tex2jax: { inlineMath: [['$','$'],['\\(','\\)']] }
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
    this.buffer = buffer; this.preview = preview;
    buffer.style.visibility = "hidden"; buffer.style.position = "absolute";
    preview.style.position = ""; preview.style.visibility = "";
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