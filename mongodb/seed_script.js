const mongoose = require("mongoose");
const pathToFaker = require.resolve("faker");
const faker = require(pathToFaker);
const User = require("./model");
const { DB_URI, TARGET_DATA_COUNT } = require("./constant");

console.log(faker.name.firstName())

async function seedData() {
  const uri = DB_URI;
  const seed_count = TARGET_DATA_COUNT;
  mongoose.set("strictQuery", false);
  mongoose
    .connect(uri, {
      useNewUrlParser: true,
      useUnifiedTopology: true,
    })
    .then(() => {
      console.log("Connected to db");
    })
    .catch((err) => {
      console.log("error", err);
    });

  let timeSeriesData = [];
  for (let i = 0; i < seed_count; i++) {
    const name = faker.name.firstName();
    const price = faker.commerce.price();
    timeSeriesData.push({ name, price });
  }

  const seedDB = async () => {
    await User.insertMany(timeSeriesData);
  };

  seedDB().then(() => {
    mongoose.connection.close();
  });
}

module.exports = {
  seedData
}
