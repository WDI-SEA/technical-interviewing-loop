const axios = require('axios')

async function findUsers() {
    try{
        let res = await axios.get('https://randomuser.me/')
        let users = res.data.forEach(user => {
            user.results
        })
    } catch (error) {
        console.log(error)
    }
}

findUsers()