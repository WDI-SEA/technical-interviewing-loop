function swapStrCase(string) {
    newArray = string.split("")
    let newLetterCase = newArray.map((letter) => {
        if (letter === letter.toUpperCase()) {
           return letter.toLowerCase()
        } else {
            return letter.toUpperCase()
        }
    })
    console.log(newLetterCase.join(""))
}

swapStrCase('Hello World')