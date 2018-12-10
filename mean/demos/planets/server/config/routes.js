const Planet = require('./../controllers/planets');

module.exports = (app) =>{
    app.get('/planets', Planet.index),
    app.post('/planets', Planet.create),
    app.get('/planets/:id', Planet.show)
}