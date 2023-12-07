//這邊必須要async funciton 因為python返回需要時間，而JS 又不會block，
//所以需要用async function 加上await去呼叫PY function

async function checkAndRedirect() {
    var inputName = document.getElementById("btnCommit").value;
    const result = await eel.strAdd(inputName)()  
    
    //最後將返回的值設定在HTML上的<p>內
    document.getElementById('pError').innerText  = result
}