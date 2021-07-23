import axios from 'axios'

const getTenRandomUsers = async () => {
    let res = await axios.get('https://randomuser.me/api/?results=10')
    let users = []
    if(res.data.results){
        users = res.data.results.map(user => {
            return {
                name: user.name.first + " " + user.name.last,
                picture: user.picture.large
            }
        })
    }
    return users
}