function hello() {
    chrome.storage.local.get("savedgood", function(items){console.log(items)});
}

document.getElementById('clickme').addEventListener('click', hello);