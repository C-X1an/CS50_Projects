var i = 0;
var name = 'Chong Xian';

function typeWriterName() {
  if (i < name.length) {
    document.getElementById("name").innerHTML += name.charAt(i);
    i++;
    setTimeout(typeWriterName, 100); // 200ms delay between each letter
  }
}

var j = 0;
var intro = "Hello, I'm";

function typeWriterIntro() {
    if (j < intro.length) {
        document.getElementById("Intro").innerHTML += intro.charAt(j);
        j++;
        setTimeout(typeWriterIntro, 100); // 200ms delay between each letter
    }
}

document.addEventListener('DOMContentLoaded', typeWriterIntro);
document.addEventListener('DOMContentLoaded', function() {
  setTimeout(typeWriterName, 1100);
})

document.addEventListener('DOMContentLoaded', function() {
  projects = document.querySelector('#about-me');
  projects.addEventListener('click', function() {
    window.location.href = "https://github.com/C-X1an?tab=repositories";
  })
  projects.addEventListener('mouseover', function() {
    projects.style.backgroundColor = "#777777";
    projects.style.color = "black";
  })
  projects.addEventListener('mouseout', function() {
    projects.style.backgroundColor = "#000000";
    projects.style.color ="white";
  })
})

document.addEventListener('DOMContentLoaded', function() {
  resume = document.querySelector('#resume');
  resume.addEventListener('click', function() {
    window.location.href = "mailto:tingcharles8@gmail.com?subject=Resume%20Request&body=Name:%0ARequest%20description:%0A%0A";
  })
  resume.addEventListener('mouseover', function() {
    resume.style.backgroundColor = "#777777";
    resume.style.color = "white";
  })
  resume.addEventListener('mouseout', function() {
    resume.style.backgroundColor = "#ffffff";
    resume.style.color ="black";
  })
})


