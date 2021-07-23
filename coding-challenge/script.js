import axios from 'axios'

const getRandomUsers = async () => {
    let res = await axios.get('https://randomuser.me/api/?results=10')
    let users = []
    if(res.data.results){
        users = res.data.results.map(user => {
            return {
                name: `${each.name.first} ${each.name.last}`,
                photo: each.picture.thumbnail
            }
        })
    }
    return users
}

getUsers()