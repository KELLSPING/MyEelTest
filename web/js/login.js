function checkAndRedirect() {
  var result = "";

  var inputName = document.getElementById("nameInput").value;
  var selectLang = document.getElementById("dropdown").value;

  // check both language and name are empty
  if (inputName.trim() === "" && selectLang.trim() === "") {
    result = '"Language" and "Name" are empty.';
    document.getElementById("pError").innerText = result;
  }
  // check language is empty
  else if (selectLang.trim() === "") {
    result = '"Language" is empty.';
    document.getElementById("pError").innerText = result;
  }
  // check name is empty
  else if (inputName.trim() === "") {
    result = '"Name" is empty.';
    document.getElementById("pError").innerText = result;
  }
  // check name is over 10 characters
  else if (inputName.length > 10) {
    result = '"Name" is too long.';
    document.getElementById("pError").innerText = result;
  } else {

    if (navigator.onLine) {
      // 如果在线，执行跳转等操作
      console.log('Button clicked, online');
      // Add your logic for redirection or other actions here
      // check name exist or not
      checkNameExist(inputName, selectLang);
    } else {
      // 如果离线，不执行跳转等操作
      console.log('Button clicked, offline');
      document.getElementById("pError").innerText = 'Internet Disconnected';
    }
    
  }
}

window.onbeforeunload = function () {
  // This function will be called when the page is about to be closed
  eel.close_login(); // Call the Python function
};

async function checkNameExist(inputName, selectLang) {
  var result = "";

  var button = document.getElementById('btnCommit');
  var spinner = document.getElementById('loading-spinner');

  button.style.visibility = 'hidden';
  spinner.style.display = 'block';

  // 等待 1 秒，作為檢查資料庫中使否依樣名字的等待時間
  await new Promise((resolve) => setTimeout(resolve, 1000));

  var ans = await eel.nameAlreadyExist(inputName)();
  console.log(result);
  if (ans === true) {
    result = '"Name" is already exist.';
    document.getElementById("pError").innerText = result;
  } else {
    // 启用按钮
    button.disabled = false;

    window.location.href =
      "chat.html?userLangSelect=" +
      encodeURIComponent(selectLang) +
      "&userInputName=" +
      encodeURIComponent(inputName);

    setTimeout(function() {
        // 显示按钮，隐藏加载圈
        button.style.visibility = 'visible';
        spinner.style.display = 'none';
      }, 1000);
    
  }
}

// Internet event listener : Reconnected
window.addEventListener('online', async function() {
  console.log("Internet connected.");
  message = 'Internet Reconnected.'

  console.log(message);

  document.getElementById("pError").innerText = '';

  var inputName = document.getElementById("nameInput").value.trim();

  await eel.get_internet_status('connect')();
  await eel.clean_user(inputName)();

  var customAlert = document.getElementById('custom-alert');
        customAlert.innerHTML = message;
        customAlert.style.display = 'block';
        customAlert.style.color = 'green';
        customAlert.style.borderColor  = 'green';
        
        setTimeout(function() {
            customAlert.style.display = 'none';
        }, 3000); // Hide after 2 seconds (adjust as needed)
});

// Internet event listener : disconnected
window.addEventListener('offline', async function() {
  message = 'Internet Disconnected.'

  console.log(message);

  await eel.get_internet_status('disconnect')();

  var customAlert = document.getElementById('custom-alert');
        customAlert.innerHTML = message;
        customAlert.style.display = 'block';

        setTimeout(function() {
            customAlert.style.display = 'none';
        }, 3000); // Hide after 2 seconds (adjust as needed)
});
