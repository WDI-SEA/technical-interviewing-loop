// import express
const express = require('express')
// import axios - node package allows basic get request
const axios = require('axios')

//define port
const PORT = 3000

// declare an instance of an app
const app = express()

// create a home route
app.get('/', (req,res) => {
    axios.get(`https://randomuser.me/api/?results=10`)
        .then((response) => {
            let data = response.data.results
            data.forEach(person => {
                let name = person.name
                let picture = person.picture
                console.log(name, picture)
            })
        })
        .catch(err => {console.log(err)})   
})

// open up a port for the app to listen on
app.listen(PORT, () => {
    console.log(`Hello from ${PORT}`)
})