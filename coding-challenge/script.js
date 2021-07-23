// #need to figure out how to call the api
// #within the api, 
// # its data.results.name.first,
// #data.results.picture.large'


const axios = require('axios')

const users = async () => {
  let res = await axios.get('http://randomuser.me/api/?results=10')
  let users = []
  if (res.data.results) {
    users = res.data.results.map(user => {
      return {
        name: user.name.first + " "+ user.name.last,
        picture: user.picture.large
      }
    })
    console.log(users)
  }
  return users
}

users()

