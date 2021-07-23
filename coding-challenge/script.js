import axios from 'axios'

const users = async() => {
    let response = await axios.get('https://randomuser.me/api/?results=10')
    let userArr = []
    for (let each of response.data.results) {
        userArr.push({
            name: `${each.name.first} ${each.name.last}`,
            picture:  each.picture.thumbnail
        })
    }
    console.log(userArr)
    return userArr
}

users()