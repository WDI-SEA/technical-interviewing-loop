const { default: axios } = require("axios");

async function peopleCall(){
    try {let res = await axios.get('https://randomuser.me/api/?results=10')
    peopleData = res.data.results
    personData = peopleData.map((person) => {
        console.log(person.name.first, person.name.last)
        console.log(person.picture.thumbnail)
    })} catch(error) {
        console.log(error)
    }
}

peopleCall()