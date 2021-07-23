// In whichevever coding language you would like please write an answer to the following problem:

// ```
// Have the function swapStrCase(string) take the string parameter and swap the case of each character. 

// For example: if string is "Hello World" the output should be hELLO wORLD. Let numbers and symbols stay the way they are.
// ```

// Write your answer in a file called `challenge-1.language_of_choice`, and save in this folder.


function swapStrCase(string) {
  let word = []
  // const makeArr = word.join().split(' ')
  //console.log(makeArr)

  for (let i = 0; i < string.length; i++) {
    //check case if char in index 
    if (string[i] === string[i].toLowerCase()) {
      //change case
      word.push(string[i].toUpperCase())
    } else {
    word.push(string[i].toLowerCase()) 
    }
  }
  return word.join('')
}

console.log(swapStrCase("Hello World"))