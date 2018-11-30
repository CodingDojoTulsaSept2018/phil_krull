// loads/imports express
var express = require('express');
// create a express instances
var app = express();
// js library for finding and joining directory locations
var path = require('path');
// js library to allow access to form data from html
var bodyParser = require('body-parser');

// new code:
var session = require('express-session');

// more new code:
// _____________________________ config the express server _______________________________
// config the use of session
app.use(session({
  secret: 'keyboardkitteh',
  resave: false,
  saveUninitialized: true,
  cookie: { maxAge: Infinity }
}))

// set the type of expected form data from client
app.use(bodyParser.urlencoded({extended: true}));

// point and set the location of all static content(html link, script, img look here)
app.use(express.static(path.join(__dirname, "./static")));

// below will be removed with angular
// setting path to where the html are located
app.set('views', path.join(__dirname, './views'));
// setting the view engine to ejs
app.set('view engine', 'ejs');
console.log(__dirname);

// _____________________________ end of config the express server _______________________________

// the request and response objects will get passes as arguements to the callback
app.get('/', function(req, res){
  let todayServer = 'Friday!';
  res.render('index', {todayClient: todayServer})
})

app.post('/users', function(req, res) {
  console.log(req.body);
  res.redirect('/');
})

// sets and starts the server
app.listen(8888, function(){
  console.log("Listening on port 8888");
})