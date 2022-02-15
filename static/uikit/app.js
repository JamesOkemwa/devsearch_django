// Invoke Functions Call on Document Loaded
document.addEventListener('DOMContentLoaded', function () {
  hljs.highlightAll();
});

// close the messages popup
let alertWrapper = document.querySelector('.alert')
let alertClose = document.querySelector('.alert__close')

if (alertWrapper) {
  alertClose.addEventListener('click', () =>
    alertWrapper.style.display = 'none'
  )
}
// let alertWrapper = document.getElementById('popup-message')
// let alertClose = document.getElementById('close-popup')

// if (alertWrapper) {
//   alertClose.addEventListener('click', function() {
//     alertWrapper.style.display = 'none'
//   })
// }
