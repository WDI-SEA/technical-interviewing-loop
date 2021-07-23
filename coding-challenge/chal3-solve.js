const countArr = arr => {
    total = 0
  for(i=0; i < arr.length; i++){
    if(typeof arr[i] !== "string"){
      arr[i].toString().split('')
      .forEach(c => {
        //   console.log(total)
          total++
      })
    } else {
        arr[i].split('')
        .forEach(char =>{
            total++
        })
    }
  }
  console.log(total)
  return total
 
}

countArr(["hello", "hi", 323])