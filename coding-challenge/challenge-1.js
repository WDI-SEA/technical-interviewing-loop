// iterate through string
// check type
    // if letter is uppercase
        // change to lowercase
        // else change to uppercase

let swapStrCase = (string) => {

    let output = ''
    for (let i = 0; i < string.length; i++) {
        if (string[i] === string[i].toLowerCase()) {
            output += string[i].toUpperCase()
        } else {
            output += string[i].toLowerCase()
        }
    }
    return output
}

console.log(swapStrCase('Hello 1#$World'))