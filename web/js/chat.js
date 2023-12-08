// 获取 URL 中的查询参数
const urlParams = new URLSearchParams(window.location.search);
const userInputName = urlParams.get('userInputName');
const userLangSelect = urlParams.get('userLangSelect');

// 顯示名字和語言在 chat.html
// document.getElementById('txtName').innerText  = userInputName;
// document.getElementById('txtLanguage').innerText  = userLangSelect;

eel.process_user_input(userInputName, userLangSelect);

// right key forbidden
document.oncontextmenu = new Function("return false");
oncontextmenu="return flase;"

// 鍵盤監聽
document.onkeydown = function(e){
  var keyNum =window.event ? e.keyCode : e.which;
  //Enter press
  if (keyNum == 13){
    send_message();
  }
}

// 這邊必須要async funciton 因為python返回需要時間，而JS 又不會block，
// 所以需要用async function 加上await去呼叫PY function
async function send_message(){
    var messageInput = document.getElementById('message-input');
    var message = messageInput.value.trim();
  
    if (message !== '') {
      // 呼叫 eel 中的 func ，func 名稱後面的 () 作為輸入參數用，最後的 () 用作取值，並將結果回傳在 result
      result = await eel.get_message(message)()
  
      var chatMessages = document.getElementById('chat-messages');
      var newMessage = document.createElement('div');
      newMessage.textContent = result;
      
      // 使用 JS 實現文字隨視窗大小縮放
      setResponsiveFontSize(newMessage, "16px");
  
      chatMessages.appendChild(newMessage);
      // Clear the input field
      messageInput.value = '';
      // Scroll to the bottom to show the latest message
      chatMessages.scrollTop = chatMessages.scrollHeight;
    }
  }
  
  eel.expose(update);
  function update(s){
    var message = s;
    if (message !== '') {
      // 呼叫 eel 中的 func ，func 名稱後面的 () 作為輸入參數用，最後的 () 用作取值，並將結果回傳在 result
  
      var chatMessages = document.getElementById('chat-messages');
      var newMessage = document.createElement('div');
      newMessage.textContent = s;
      chatMessages.appendChild(newMessage);
      // Clear the input field
      // Scroll to the bottom to show the latest message
      chatMessages.scrollTop = chatMessages.scrollHeight;
    }
  }
  
  
  function mouseDown(){
      var button = document.getElementById('btn-send-audio');
      button.classList.add('clicked');
      eel.on_press()()
  }
  
  function mouseUp(){
    var button = document.getElementById('btn-send-audio');
    var chatMessages = document.getElementById('chat-messages');
    var newMessage = document.createElement('div');
    button.classList.remove('clicked');
    eel.on_release()()
  }
  
  eel.expose(showText);
  function showText(s){
      var messageInput = document.getElementById('message-input');
      messageInput.value=s;
  }
  
  function setResponsiveFontSize(element, initialFontSize) {
    // Set the initial font size (optional)
    element.style.fontSize = initialFontSize;
  
    // Add a listener for window resize events to update font size responsively
    function updateFontSize() {
      // Get the current viewport width
      var viewportWidth = window.innerWidth || document.documentElement.clientWidth;
  
      // Adjust the font size based on the viewport width
      if (viewportWidth < 600) {
        element.style.fontSize = "16px";
      } else if (viewportWidth < 1080) {
        element.style.fontSize = "24px";
      } else {
        element.style.fontSize = "32px";
      }
    }
  
    // Add the new message div to the chat-messages container
    var chatMessages = document.getElementById('chat-messages');
    chatMessages.appendChild(element);
  
    // Trigger the resize event once to set the initial font size
    updateFontSize();
  
    // Add event listener for window resize
    window.addEventListener('resize', updateFontSize);
  }
  