var numberOfButtons = document.querySelectorAll('.drum').length;

for (var i = 0; i < numberOfButtons; i++) {

    document.querySelectorAll(".drum")[i].addEventListener('click', function () {
        
        var sound = new Audio('sounds/tom-1.mp3');
        
        sound.play();

        this.style.color = 'white'

    });
}