// Have the function swapStrCase(string) take the string parameter and swap the case of each character. 

// For example: if string is "Hello World" the output should be hELLO wORLD. Let numbers and symbols stay the way they are.

function swapStrCase(string) {
    let word = '';
    for( i = 0; i < string.length; i++) {
        if(string[i] == string[i].toLowerCase()) {
            word = word + string[i].toUpperCase();
        } else {
            word = word + string[i].toLowerCase();
        }
    } 
    return word;
}

console.log(swapStrCase("Hello12 World!"))