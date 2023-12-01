aboutHeading = document.getElementsByClassName('about-heading')
aboutText = document.getElementsByClassName('about-text')

function toggleAboutText() {
    console.log(aboutHeading[0].classList)
    aboutHeading[0].classList.toggle('about-heading-inactive')
    aboutText[0].classList.toggle('about-text-inactive')
}