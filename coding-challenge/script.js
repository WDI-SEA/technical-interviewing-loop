const axios = require('axios')

// // Using the [Random User Generator API](https://randomuser.me/), query for a list of 10 users and for each user and return an array of objects with their profile photo and name.

let tenUsers = async () => {
    let users = []
    let res = await axios.get('https://randomuser.me/api/?results=10')

    users = res.data.results.map(user => {
        console.log("🔥")
        return {
            name: user.name,
            photo: user.picture
        }
    })
    console.log(users)
    return users
}

tenUsers()
