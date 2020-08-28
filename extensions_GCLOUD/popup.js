window.onload = changingHTML;

// Further function calls content.js which has the google extension functionality
function classify() 
	{chrome.tabs.executeScript(null, { file: "content.js" });
	};
	
function classifyshort() 
	{chrome.tabs.executeScript(null, { file: "contentshort.js" });
	};	
	
function changingHTML() {
  var x = document.getElementById("window2");
  var y = document.getElementById("window1");
  if (x.style.display == "none" || x.display == '') {
    x.style.display = "block";
	y.style.display = "none";
  } else {
    x.style.display = "none";
  }
}

function button1() {
	changingHTML();
	classify();
}

function button2() {
	changingHTML();
	classifyshort();
}

// When button is clicked then the function classify() is executed
document.getElementById('clickme').addEventListener('click', button1);
// When button is clicked then the function classifyshort() is executed
document.getElementById('clickmeshort').addEventListener('click', button2);



