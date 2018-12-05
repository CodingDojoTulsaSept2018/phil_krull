const mongoose = require('mongoose');

const QuoteSchema = new mongoose.Schema({
  name: {
    type: String,
    required: [true, 'Quote name is required!'],
  },
  quote: {
    type: String,
    required:[true, 'Quote content is required!'],
  },
  likes: {
    type: Number,
    default: 0
  }
}, {timestamps: true})
// setter
mongoose.model('Quote', QuoteSchema);
