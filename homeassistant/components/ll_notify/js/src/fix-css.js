/**
 * Fix the default text color for alertify.
 *
 * This quite a hack. I'm not sure what's going on but right now I just want it fixed.
 *
 * DevNotes
 * In Dark Mode, HA / Lovelace will be black. Alertify's dialog's are white with black text.
 * BUT, in HA, the text color is NOT set, and it inherits a white text - so you get white on white - invisibile.
 * Alertify does NOT seem to do this incorrectly in general. (I played around with it in JS Fiddle.)
 *
 * Instead, it seems to be something about how HA sets it's color internally with the variable
 * '--text-primary-color'.
 *
 * My logic here is simple - get the text color from the <home-assistant> element and set a style.
 * (You can't just do getElementByClassName because the alertify dom element isn't created til needed.)
 *
 * Possible solution: Add alertify to the shadow DOM under <home-assistant> instead of to the root DOM.
 */

export function fixCSS() {
  try {
    let textColor = getComputedStyle(
      document.getElementsByTagName("home-assistant")[0]
    )
      .getPropertyValue("--text-primary-color")
      .trim()

    if (textColor == "#ffffff") {
      // If white, set to black
      textColor = "#000000"
    }

    const newStyle = `
        .alertify {
            color: ${textColor};
        }

        .alertify-notifier {
            color: ${textColor};
        }
    `

    // https://stackoverflow.com/a/15494200/1400991
    const style = document.createElement("style")
    if (style.styleSheet) {
      style.styleSheet.cssText = newStyle
    } else {
      // This is the path that is taken.
      style.appendChild(document.createTextNode(newStyle))
    }
    document.getElementsByTagName("head")[0].appendChild(style)
  } catch (err) {
    console.error("lovelace_notify_card: Error fixing CSS", err)
  }
}
