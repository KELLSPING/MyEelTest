//這邊必須要async funciton 因為python返回需要時間，而JS 又不會block，
//所以需要用async function 加上await去呼叫PY function
async function btn_click(){ 
    
    //呼叫的方式，就是加上eel.加上剛剛被expose PY function的名稱然後多加()輸入參數，最後加()取值
    result = await eel.say_something('Hello word')()  
    
    //最後將返回的值設定在HTML上的<p>內
    document.querySelector('p').textContent = result
}