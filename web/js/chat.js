// 获取 URL 中的查询参数
const urlParams = new URLSearchParams(window.location.search);
const userInputName = urlParams.get('userInputName');
const userLangSelect = urlParams.get('userLangSelect');

document.getElementById('txtName').innerText  = userInputName;
document.getElementById('txtLanguage').innerText  = userLangSelect;