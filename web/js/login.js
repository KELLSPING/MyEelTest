//這邊必須要async funciton 因為python返回需要時間，而JS 又不會block，
//所以需要用async function 加上await去呼叫PY function

function checkAndRedirect() {
    var result = "" 

    var inputName = document.getElementById("nameInput").value;
    var selectLang = document.getElementById("dropdown").value;

    if (inputName.trim() === "" && selectLang.trim() === "") {
        result = "\"Language\" and \"Name\" are empty."
        document.getElementById('pError').innerText  = result
    } else if (inputName.trim() === "") {
        result = "\"Name\" is empty."
        document.getElementById('pError').innerText  = result
    } else if (selectLang.trim() === "") {
        result = "\"Language\" is empty."
        document.getElementById('pError').innerText  = result
    } else {
        window.location.href = "chat.html?userLangSelect=" + encodeURIComponent(selectLang) + "&userInputName=" + encodeURIComponent(inputName);
    }
}