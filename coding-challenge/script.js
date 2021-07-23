const axios = require('axios')

let userList 

function getUsers(){
    axios.get('https://randomuser.me/api/?results=10&inc=gender,name,picture')
    .then(response => {
        console.log(response.data.results)
        userList = response.data.results
    })
    .catch(err => {
        console.log(err)
    })
        
    
}    

getUsers()