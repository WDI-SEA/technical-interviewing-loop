const axios = require('axios');
// **Full credit to @Emma Bostian for this question.**

// Using the [Random User Generator API](https://randomuser.me/), query for a list of 10 users and for each user and return an array of objects with their profile photo and name.

// Write your script in Javascript, and submit in a file called `script.js`.

async function randomApi() {
  try {
    getUsers = []
    let api = await axios.get('https://randomuser.me/api/?results=10')
    //console.log(api.data)

    let users = api.data.results
    getUsers = users.map( user => {
      //console.log(user, "😈")
      return {
        name: user.name,
        picture: user.picture.medium
        
      }
    })
    console.log(getUsers)
    return getUsers
  } catch (e) {
    console.log(e)
  }

}

randomApi()
