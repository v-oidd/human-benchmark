/* Bot for https://humanbenchmark.com/tests/reactiontime
 * Paste the script in the console once you are on the above link, before you begin the test
 * Guaranteed 1-3ms & 100.0% percentile
 */

function triggerMouseDown(element) {
    const mouseDownEvent = new MouseEvent('mousedown', {
        'view': window,
        'bubbles': true,
        'cancelable': true,
    })
    element.dispatchEvent(mouseDownEvent);
}

// Click screen if screen is green or blue
function callback(mutationList) {
	for (const mutation of mutationList) {
		if (mutation.attributeName === "class") {
			const target = mutation.target;
            if (target.classList.contains('view-go') || target.classList.contains('view-result')) {
				triggerMouseDown(target);
			}
		}
	}
};

const observer = new MutationObserver(callback);
const screenElement = document.querySelector('.e18o0sx0')
const config = {
	attributeOldValue: true,
	attributes: true,
	attributeFilter: ['class']
}

observer.observe(screenElement, config);
