// get quote controller
const Quote = require('./../controllers/quotes')
// access a url, and calls the callback
module.exports = (app) => {
    app.get('/', Quote.index)
    app.post('/quotes', Quote.create)
    app.get('/quotes', Quote.getAll)
    app.post('/quotes/like/:id', Quote.update)
}