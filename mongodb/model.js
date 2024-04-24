const mongoose = require("mongoose");
const userSchema = new mongoose.Schema({
    name:{
     type:String,
     required:true   
    },
    price:{
        type:Number,
        required:true
    }
})
const User = mongoose.model("User",userSchema)
module.exports = User;