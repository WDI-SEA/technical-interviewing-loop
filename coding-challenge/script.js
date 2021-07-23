import axios from 'axios'

const getUsers = async () => {
    let response = await axios.get('https://randomuser.me/api/?results=10')

    let users = []

    for(let each of response.data.results) {
        console.log("🦄")
       users.push({
           name: `${each.name.first} ${each.name.last}`,
           photo: each.picture.thumbnail
       })
    }

    return users
}

getUsers()