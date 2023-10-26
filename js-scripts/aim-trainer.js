/* Bot for https://humanbenchmark.com/tests/aim
 * Paste the script in the console once you are on the above link, before you click start
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

// Click all buttons
for (let i = 0; i <= 30; i++) {
	triggerMouseDown(document.getElementsByClassName('css-q4kt6s')[0])
}
