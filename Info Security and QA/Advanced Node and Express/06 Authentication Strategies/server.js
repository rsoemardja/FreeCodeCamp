"use strict";

const express = require("express");
const fccTesting = require("./freeCodeCamp/fcctesting.js");
const bodyParser = require("body-parser");
const session = require("express-session");
const passport = require("passport");
const db = require("mongodb");
const mongo = db.MongoClient;
const ObjectID = db.ObjectID;
const LocalStrategy = require('passport-local');
const app = express();

fccTesting(app); //For FCC testing purposes
app.use("/public", express.static(process.cwd() + "/public"));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.set("view engine", "pug");

app.use(
    session({
        secret: process.env.SESSION_SECRET,
        resave: true,
        saveUninitialized: true
    })
);
app.use(passport.initialize());
app.use(passport.session());

passport.serializeUser((user, done) => {
    done(null, user._id);
});
passport.deserializeUser((id, done) => {
    db.collection("users").findOne({ _id: new ObjectID(id) }, (err, doc) => {
        done(null, doc);
    });
});

mongo.connect(process.env.DATABASE, (err, db) => {
    if (err) {
        console.log("Database error: " + err);
    } else {
        console.log("Successful database connection");

        //serialization and app.listen
    }
});

passport.use(new LocalStrategy(
    function (username, password, done) {
        db.collection('users').findOne({ username: username }, function (err, user) {
            console.log('User ' + username + ' attempted to log in.');
            if (err) { return done(err); }
            if (!user) { return done(null, false) }
            if (password !== user.password) { return done(null, false); }
            return done(null, user);
        });
    }
));

app.route("/").get((req, res) => {
    //Change the response to render the Pug template
    res.render(process.cwd() + "/views/pug/index.pug", {
        title: "Hello",
        message: "Please login"
    });
});

app.listen(process.env.PORT || 3000, () => {
    console.log("Listening on port " + process.env.PORT);
});
