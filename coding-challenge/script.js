const axios = require('axios')

// **Full credit to @Emma Bostian for this question.**

// Using the [Random User Generator API](https://randomuser.me/), query for a list of 10 users and for each user and return an array of objects with their profile photo and name.

// Write your script in Javascript, and submit in a file called `script.js`.
let users
let x = axios.get('https://randomuser.me/api/?results=10')
.then((response) => {
    // console.log(response.data.results)
    users = response.data.results
    

    let userArray = []
    for(user of users){
        userArray.push({"name": user.name.first +" "+ user.name.last, "picture": user.picture.medium})
    }
    
    console.log(userArray)   


}).catch((err) => {
    console.log(err)
})
console.log(users)

