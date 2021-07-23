const axios = require ('axios')


async function getUsers() {
    try {
        const users = await axios.get(`https://randomuser.me/api/?results=10&inc=name,picture`)
        console.log(users.data.results)
    } catch (err) {
        console.log(err)
    }    
}

getUsers()