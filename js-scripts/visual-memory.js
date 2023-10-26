/* Bot for https://humanbenchmark.com/tests/memory
 * Paste the script in the console once you are on the above link, before you click start
 * NOTE: Click the red-black button at the right of the screen to stop the script
 */

const triggerMouseDown = (element) => {
	const mouseDownEvent = new MouseEvent('mousedown', {
		'view': window,
		'bubbles': true,
		'cancelable': true,
	})
	element.dispatchEvent(mouseDownEvent);
}

const waitUntil = (condition, checkInterval=50) => {
	return new Promise(resolve => {
		let interval = setInterval(() => {
			if (!condition()) return;
			clearInterval(interval);
			resolve();
		}, checkInterval)
	})
}

// Button to stop the script
const checkbox = document.createElement("input");
checkbox.type = "checkbox";
checkbox.style.position = "fixed";
checkbox.style.top = "50%";
checkbox.style.right = "10px";  
checkbox.style.appearance = "none"; 
checkbox.style.border = "2px solid #FF0000"; 
checkbox.style.borderRadius = "50%"; 
checkbox.style.width = "40px"; 
checkbox.style.height = "40px"; 
checkbox.style.backgroundColor = "white"; 
checkbox.style.cursor = "pointer";

let breakLoop = false;

checkbox.addEventListener("change", function() {
  if (this.checked) {
    document.body.removeChild(checkbox);
	breakLoop = true;
  }
});

document.body.appendChild(checkbox);

let startButton = document.querySelector('.css-de05nr');
// Click start button if the user hasn't already clicked it
startButton && triggerMouseDown(startButton);

async function start() {
	while (!breakLoop) {
		// Wait for flashing squares to appear before storing them
		await waitUntil(() => document.querySelectorAll('div.active').length > 0);
		let square_flashes = document.querySelectorAll('div.active');

		// Wait for flashing squares to disappear before clicking them
		await waitUntil(() => document.querySelectorAll('div.active').length == 0);
		square_flashes.forEach((square) => triggerMouseDown(square));
	}

}

start();
