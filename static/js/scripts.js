
$(document).ready(function(){
  $(".navbar a, footer a[href='#myPage']").on('click', function(event) {
    if (this.hash !== "") {
      // Prevent default anchor click behavior
      event.preventDefault();
      var hash = this.hash;
      // Using jQuery's animate() method to add smooth page scroll
      $('html, body').animate({
        scrollTop: $(hash).offset().top
      }, 900, function(){

        window.location.hash = hash;
      });
    } // End if
  });
  
  $(window).scroll(function() {
    $(".slideanim").each(function(){
      var pos = $(this).offset().top;
      var winTop = $(window).scrollTop();
        if (pos < winTop + 600) {
          $(this).addClass("slide");
        }
    });
  });
})


document.getElementById("apply-button").addEventListener("click", function() {
    window.location.href = "/apply"; 
  });
  
window.addEventListener('scroll', function() {
  var navbar = document.getElementById('navbar');
  if (window.scrollY > 50) {
      navbar.classList.add('scrolled');
  } else {
      navbar.classList.remove('scrolled');
  }
});

// function resetForm() {
//             document.getElementById('loan-application-form').reset();
//             localStorage.removeItem('formData');
//         }

//         function saveFormData() {
//             const formData = new FormData(document.getElementById('loan-application-form'));
//             const data = {};
//             formData.forEach((value, key) => data[key] = value);
//             localStorage.setItem('formData', JSON.stringify(data));
//         }

//         function loadFormData() {
//             const data = localStorage.getItem('formData');
//             if (data) {
//                 const formData = JSON.parse(data);
//                 for (const [key, value] of Object.entries(formData)) {
//                     const input = document.querySelector(`[name="${key}"]`);
//                     if (input) {
//                         input.value = value;
//                     }
//                 }
//             }
//         }

//         window.onload = function() {
//             resetForm(); // Clear form on initial load
//             loadFormData(); // Load form data if available
//         };

//         window.addEventListener('pageshow', function(event) {
//             if (event.persisted) {
//                 resetForm(); // Clear form if restored from cache
//             }
//         });

//         document.getElementById('loan-application-form').addEventListener('input', saveFormData);