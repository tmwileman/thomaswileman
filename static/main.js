window.MathJax = {
    menuSettings: {
      autocollapse: true
    }
  };
  
  script = document.createElement('script');
  script.type = 'text/javascript';
  script.async = true;
  script.onload = function() {
    // remote script has loaded
  };
  script.src = 'https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=MML_CHTML-full';
  document.getElementsByTagName('head')[0].appendChild(script);
  var box = document.getElementById('box');
  var rng = document.getElementById('rngWidth');
  var note = document.getElementById('rngValue');
  rng.onchange = function() {
    box.style.width = this.value + 'px';
    MathJax.Extension["auto-collapse"].resizeHandler()
    note.innerHTML = this.value + 'px';
  }