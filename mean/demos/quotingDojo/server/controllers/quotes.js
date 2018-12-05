// get the model instance we are using
// getter
const mongoose = require('mongoose');
const Quote = mongoose.model('Quote');

module.exports = {
    // this would contain the restfull routing
    index: (req, res)=>{
        res.render('index', { errors:undefined });
      },
      create: (req, res)=>{
        let quote = new Quote({name: req.body.name, quote: req.body.quote})
        quote.save()
        .then((success)=>{
          res.redirect('/quotes');
        })
        .catch((err)=>{
          console.log(err);
          console.log('-'.repeat(90));
          console.log(err.errors.name.message);
          res.render('index', { errors: err.errors.name.message })
        })
      },
      getAll: (req, res)=>{
        Quote.find({}, null, {sort: '-likes'}, (err, quotes)=>{
          if(err){
            console.log(err);
          } else {
            res.render('quotes', {all_quotes:quotes});
          }
        })
      },
      update: (req, res)=>{
        console.log(`the id is ${req.params.id}`);
        res.redirect('/quotes')
        Quote.findOneAndUpdate({_id: req.params.id}, {$inc:{'likes':1}}, (err, quote)=>{
          console.log(`the error is ${err}`);
          console.log(`the quote is ${quote}`);
        })
      }
}