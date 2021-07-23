arr = [453, "hello", 293, true]

function arrayCounter(array) {
    let sepArray = array.map((value) => {
        let stringVal = value.toString()
        let splitVal = stringVal.split("")
        let nums = splitVal.push()
        return nums
    })
    let sum = sepArray.reduce(function (accumulator, currentValue){
        return accumulator + currentValue
    })
    console.log(sum)
}

arrayCounter(arr)