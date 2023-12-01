const buttonColors = ["red", "blue", "green", "yellow"];

var gamePattern = [];
var userClickedPattern = [];

var gameIsOn = false;
var level = 0;

function playSound(color) {
    switch (color) {
        case 'red':
            var audioRed = new Audio('sounds/red.mp3');
            audioRed.play();
            break;
    
        case 'blue':
            var audioBlue = new Audio('sounds/blue.mp3');
            audioBlue.play();
            break;
        case 'green':
            var audioGreen = new Audio('sounds/green.mp3');
            audioGreen.play();
            break;
    
        case 'yellow':
            var audioYellow = new Audio('sounds/yellow.mp3');
            audioYellow.play();
            break;

    default: console.log(color)
}}

function nextSequence() {
    level = level + 1

    $('h1').text('Level: ' + level)

    randomNumber = Math.floor(Math.random()*4);

    randomChosenColor = buttonColors[randomNumber];

    $('#' + randomChosenColor).fadeOut(100).fadeIn(100)

    playSound(randomChosenColor)

    gamePattern.push(randomChosenColor);

    userClickedPattern = [];
}

function gameOver() {
    var audioWrong = new Audio('sounds/wrong.mp3');
    audioWrong.play();

    $('body').attr('class', 'game-over');

    setTimeout(function() {
        $('body').removeAttr('class', 'game-over');;
    }, 200);

    $('h1').text('Game Over, Press "A" To Restart');

    gameIsOn = false;

    gamePattern = [];

    level = 0;
}

// Game Start
$(document).keypress(function (e) {
    var letter = e.key

    if (gamePattern.length == 0){
        if (letter == 'a') {
            gameIsOn = true;
            nextSequence();
        }
    }
});

$('.btn').click(function (e) {
    if (gameIsOn){
        userChosenColor = $(this).attr('id')

        $('#' + userChosenColor).fadeOut(100).fadeIn(100)

        playSound(userChosenColor)

        userClickedPattern.push(userChosenColor)

        checkRules(level)

    }
});

function checkRules(currentLevel) {

    userColor = userClickedPattern.slice(-1)[0];

    gameColor = gamePattern.slice(0, userClickedPattern.length).slice(-1)[0];

    if (userColor == gameColor) {
        if (userClickedPattern.length == currentLevel) {
                setTimeout(function() {
                    nextSequence();
                }, 1000);
            } 
    } else {
        gameOver();
    }
}