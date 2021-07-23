const axios = require('axios')

const findRando = () => {
    randoArray = []

    axios.get("https://randomuser.me/api/?results=10")
        .then(res => {
            let results = res.data.results
            for (i = 0; i < results.length; i++) {
                randoArray[i] = {
                    name: `${results[i].name.title} ${results[i].name.first} ${results[i].name.last}`,
                    picture: results[i].picture.large
                }
            }
            console.log(randoArray)
        }) 
        .catch(err => console.log(err))
}

findRando()
    
