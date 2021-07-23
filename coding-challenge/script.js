//Using the [Random User Generator API](https://randomuser.me/), 
//query for a list of 10 users and for each user and return an array of objects 
//with their profile photo and name.
 const axios = require('axios')

 axios.get('https://randomuser.me/api/?results=10')
    .then(response => {
        const users = response.data.results
        users.forEach(user => {
            console.log(user.name.first, user.name.last, user.picture.thumbnail)
        })
    })
