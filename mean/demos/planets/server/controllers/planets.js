const mongoose = require('mongoose');
const Planet = mongoose.model('Planet');

module.exports = {
    index: (req, res)=>{
        // show all
        Planet.find({}, (err, planets)=>{
            if(err) {
                res.send(err);
            } else {
                res.json({message: true, allPlanets: planets});
            }
        })
    },
    create: (req, res)=>{
        // create one
        Planet.create(req.body, (err, planet)=>{
            if(err) {
                res.send(err);
            } else {
                res.json({message: true, addedPlanet: planet});
            }
        })
    },
    show: (req, res)=>{
        // show one
        Planet.findById(req.params.id, (err, planet)=>{
            if(err) {
                res.send(err);
            } else {
                res.json({message: true, onePlanet: planet});
            }
        })
    }
}