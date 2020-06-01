'use strict';

const express = require('express');
const bodyParser = require('body-parser');
const fccTesting = require('./freeCodeCamp/fcctesting.js');

const session = require('express-session');
const mongo = require('mongodb').MongoClient;

const bcrypt = require('bcrypt');
const routes = require('./routes.js');
const auth = require('./auth.js');

const app = express();

const io = require('socket.io');


mongo.connect(process.env.MONGO_URI, (err, db) => {
    if (err) {
        console.log('Database error: ' + err);
    } else {
        console.log('Successful database connection');


        fccTesting(app); //For FCC testing purposes
        app.use('/public', express.static(process.cwd() + '/public'));
        app.use(bodyParser.json());
        app.use(bodyParser.urlencoded({ extended: true }));

        app.set('view engine', 'pug');




        /*
        
        io.on('connection', socket => {
      console.log('A user has connected');
    });
        
        */





        //
        //
        //
        //
        //
        // AUTH

        const session = require('express-session');
        const passport = require('passport');
        const ObjectID = require('mongodb').ObjectID;
        const LocalStrategy = require('passport-local');
        const bcrypt = require('bcrypt');
        const GitHubStrategy = require('passport-github').Strategy;



        app.use(session({
            secret: process.env.SESSION_SECRET,
            resave: true,
            saveUninitialized: true,
        }));
        app.use(passport.initialize());
        app.use(passport.session());


        passport.serializeUser((user, done) => {
            done(null, user._id);
        });
        passport.deserializeUser((id, done) => {
            db.collection('users').findOne(
                { _id: new ObjectID(id) },
                (err, doc) => {
                    done(null, doc);
                }
            );
        });



        passport.use(new LocalStrategy(
            function (username, password, done) {
                db.collection('users').findOne({ username: username }, function (err, user) {
                    console.log('User ' + username + ' attempted to log in.');
                    if (err) { return done(err); }
                    if (!user) { return done(null, false); }
                    if (!bcrypt.compareSync(password, user.password)) { return done(null, false); }
                    return done(null, user);
                });
            }
        ));



        //passport.use(new GitHubStrategy({
        //    clientID: process.env.GITHUB_CLIENT_ID,
        //    clientSecret: process.env.GITHUB_CLIENT_SECRET,
        //    callbackURL: 'https://advanced-node-and-express-challenges-2019.glitch.me/auth/github/callback'
        //  },
        //  function(accessToken, refreshToken, profile, cb) {
        //      console.log(profile);

        //      db.collection('socialusers').findAndModify(
        //          {id: profile.id},
        //          {},
        //          {$setOnInsert:{
        //              id: profile.id,
        //              name: profile.displayName || 'John Doe',
        //              photo: profile.photos[0].value || '',
        //              email: profile.emails[0].value || 'No public email',
        //              created_on: new Date(),
        //              provider: profile.provider || ''
        //          },$set:{
        //              last_login: new Date()
        //          },$inc:{
        //              login_count: 1
        //          }},
        //          {upsert:true, new: true},
        //          (err, doc) => {
        //              return cb(null, doc.value);
        //          }
        //      );  
        //  
        //  }
        //));  








        ////
        //
        //
        //
        //
        //
        //
        //
        //
        //
        // ROUTES


        app.route('/auth/github')
            .get(passport.authenticate('github'));

        app.route('/auth/github/callback')
            .get(passport.authenticate('github', { failureRedirect: '/' }), (req, res) => {
                res.redirect('/profile');
            });


        app.route('/')
            .get((req, res) => {
                res.render(process.cwd() + '/views/pug/index.pug', { title: 'Hello', message: 'Please login', showLogin: true, showRegistration: true });
            });

        app.route('/login').post(

            passport.authenticate('local', { failureRedirect: '/' }),
            function (req, res) {
                res.redirect('/profile');
            }

        );

        function ensureAuthenticated(req, res, next) {
            if (req.isAuthenticated()) {
                return next();
            }
            res.redirect('/');
        };
        app.route('/profile')
            .get(ensureAuthenticated, (req, res) => {
                res.render(process.cwd() + '/views/pug/profile', { username: req.user.username });
            });

        app.get('/logout', function (req, res) {
            req.logout();
            res.redirect('/');
        });

        app.route('/register')
            .post((req, res, next) => {
                db.collection('users').findOne({ username: req.body.username }, function (err, user) {
                    if (err) {
                        next(err);
                    } else if (user) {
                        res.redirect('/');
                    } else {
                        let hash = bcrypt.hashSync(req.body.password, 12);
                        db.collection('users').insertOne(
                            {
                                username: req.body.username,
                                password: hash
                            },
                            (err, doc) => {
                                if (err) {
                                    res.redirect('/');
                                } else {
                                    next(null, user);
                                }
                            }
                        )
                    }
                })
            },
                passport.authenticate('local', { failureRedirect: '/' }),
                (req, res, next) => {
                    res.redirect('/profile');
                }
            );



        app.use((req, res, next) => {
            res.status(404)
                .type('text')
                .send('Not Found');
        });





        //
        //
        //
        //
        //
        //
        //
        //
        //
        //




        app.listen(process.env.PORT || 3000, () => {
            console.log("Listening on port " + process.env.PORT);
        });


    }
});