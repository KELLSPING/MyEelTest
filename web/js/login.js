function checkAndRedirect() {
    var result = "" 

    var inputName = document.getElementById("nameInput").value;
    var selectLang = document.getElementById("dropdown").value;

    // check both language and name are empty
    if (inputName.trim() === "" && selectLang.trim() === "") {
        result = "\"Language\" and \"Name\" are empty."
        document.getElementById('pError').innerText  = result
    } 
    // check language is empty
    else if (selectLang.trim() === "") {
        result = "\"Language\" is empty."
        document.getElementById('pError').innerText  = result
    } 
    // check name is empty
    else if (inputName.trim() === "") {
        result = "\"Name\" is empty."
        document.getElementById('pError').innerText  = result
    } 
    // check name is over 10 characters
    else if (inputName.length > 10) {
        result = "\"Name\" is too long."
        document.getElementById('pError').innerText  = result
    } else {
        window.location.href = "chat.html?userLangSelect=" + encodeURIComponent(selectLang) + "&userInputName=" + encodeURIComponent(inputName);
    }
}

window.onbeforeunload = function() {
    // This function will be called when the page is about to be closed
    eel.close_login();  // Call the Python function
  };