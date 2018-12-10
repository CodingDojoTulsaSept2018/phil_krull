const mongoose = require('mongoose');

const PlanetSchema = new mongoose.Schema({
    name: {type: String, required: [true, 'Planet must have a name']},
    size: {type: Number, required: [true, 'Planet must have a size']},
    moons: {type: Number, default: 0}
}, {timestamps: true});

mongoose.model('Planet', PlanetSchema);