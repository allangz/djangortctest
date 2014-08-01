var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);
var redis = require("redis");
var sub = redis.createClient();

//Subscribe to the Redis chat channel
sub.subscribe('quote');

io.on('connection', function(socket){
console.log('a user connected');  
   sub.on('message', function(channel, message){
        console.log(message);
        socket.send(message);
   });
});

http.listen(4000, function(){
  console.log('listening on *:4000');
});
