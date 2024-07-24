# Tutorial: making a minimal Chrome extension

Usually, the way most Chrome extensions go is the following:
- You list the webpages on which you want the extension to be activated. For every page, you list the JS script(s) from the `scripts` folder.
- Whenever the user opens one of the listed webpages, the corresponding JS scripts get injected into the page.
- The injected JS scripts can execute whatever JS code you set! This enables practically any kind of change.

## Structure Chrome extensions

the `manifest.json` file contains all settings of our extension, as well as links to all JavaScript scripts that will be running on the web pages we choose. It also lists on which webpages the scripts will be activated.

the `popup_script` folder contains all the JS and HTML code that will support the popup of the extension (a small window that opwns when you click on the icon of the extension). This window usually contains user-editable settings of the extension.

the `scripts` folder contains all JS scripts to be run on web pages of choice. 

the `assets` folder is reserved for all kinds of images, icons, etc, to be used in the extension.

## Importing the extension

Currently, this extension is configured to output "Hello World" when and only when visiting the ULTA website, [www.ultacademy.org](www.ultacademy.org). This is achieved by the JS file `scripts/example_script.js`.

To run this extension in Chrome (or any web browser on Chromium - for example, Arc), use this tutorial to [load an Unpacked extension](https://developer.chrome.com/docs/extensions/get-started/tutorial/hello-world#load-unpacked)