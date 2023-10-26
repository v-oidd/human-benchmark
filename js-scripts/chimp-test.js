/* Bot for https://humanbenchmark.com/tests/chimp
 * Paste the script in the console once you are on the above link
 * NOTE: 41 is the maximum possible score
 */

// Auto click continue button when it appears
const observer = new MutationObserver(() => {
    const continueButton = document.querySelector('.css-de05nr');
    if (continueButton) {
        continueButton.click();
    }
}); 


observer.observe(document, {
    childList: true,
    subtree:   true
});

let startButton = document.querySelector('.e19owgy710');
// Click start button if the user hasn't already clicked it
startButton && startButton.click();

let buttonCount = 4;

while (buttonCount < 41)
{
    // Click all numbered buttons in order
    for (let i = 1; i <= buttonCount; i++) {
        const numberButton = document.querySelector(`div[data-cellnumber="${i}"]`);
        if (numberButton) {
            numberButton.click();
        }
    }
    buttonCount++;
    // Wait for continue button to disappear before next iteration
    while (document.querySelector('.css-de05nr')) {
        await new Promise(r => setTimeout(r, 4));
    }
}
