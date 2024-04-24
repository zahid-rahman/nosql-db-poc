# NoSQL db POC

## :white_check_mark: Mongodb setup steps

- First you have to be ensure `docker` installed on your machine
- go to mongodb folder ```cd docker-setup/mongo```
- run this command line ```docker-compose up -d``` or ```docker compose up -d```
- view your container status ```docker ps```
- now go back to root folder and go to `mongobd` folder. run this ```cd ..``` and then ```cd ./mongodb```
- Now run ```yarn seed:mongo```

⚡ To view the database install mongodb compass (DBMS) and paste this mongodb uri ```mongodb://localhost:27017/test_db```
