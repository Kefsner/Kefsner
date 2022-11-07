function add(num1, num2) {
    return num1 + num2
}

function subtract(num1, num2) {
    return num1 - num2
}

function multiply(num1, num2) {
    return num1 * num2
}

function divide(num1, num2) {
    return num1 / num2
}

function calculator(num1, num2, operation) {
    return operation(num1, num2);
}

for (var i = 0; i < 10; i++) {
    button = 'n' + i.toString()
    document.getElementsByClassName(button)[0].addEventListener('click', function () {
        document.querySelector('.current').innerHTML += this.innerHTML;
    })
}

for (var i = 1; i < 5; i++) {
    button = 'o' + i.toString()
    document.getElementsByClassName(button)[0].addEventListener('click', function () {
        if (document.querySelector('.answer').innerHTML == 0) {
            var num1 = document.querySelector('.current').innerHTML
            document.querySelector('.current').innerHTML = '';
            document.querySelector('.answer').innerHTML = num1 + '\t' + this.innerHTML;
        } else {
            document.querySelector('.answer').innerHTML = document.querySelector('.answer').innerHTML + 100;
        }

    })
}
