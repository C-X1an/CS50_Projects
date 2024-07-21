document.addEventListener('DOMContentLoaded', function() {
    logos = document.querySelectorAll('#twitter, #discord, #gmail, #github, #linkedin');
    logos.forEach(function(logo) {
      logo.addEventListener('mouseover', function() {
        logo.style.color = 'white';
      })
      logo.addEventListener('mouseout', function() {
        logo.style.color = 'black';
      })
    })
  })

document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('video').playbackRate = 0.5;
})
