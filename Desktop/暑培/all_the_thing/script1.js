// 获取锚点元素
const link = document.getElementById("myLink");

// 添加点击事件监听器
link.addEventListener("click", function(event) {
  event.preventDefault(); // 阻止默认跳转行为
  // 在这里执行希望触发的操作
  let x= "dahkjf";
  alert(x);
  console.log("点击事件被触发了");
});