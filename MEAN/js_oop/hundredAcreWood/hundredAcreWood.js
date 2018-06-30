var tigger = {character: "Tigger"};
var pooh = {character: "Winnie the Pooh"};
var piglet = {character: "Piglet"};
var bees = {character: "Bees"};
var owl = {character: "Owl"};
var christopher = {character: "Christopher Robin"};
var rabbit = {character: "Rabbit"};
var gopher = {character: "Gopher"};
var kanga = {character: "Kanga"};
var eeyore = {character: "Eeyore"};
var heffalumps = {character: "Heffalumps"};

tigger.north = pooh;
pooh.south = tigger;
pooh.west = piglet;
pooh.east = bees;
pooh.north = christopher;
bees.west = pooh;
bees.north = rabbit;
piglet.east = pooh;
piglet.north = owl;
owl.south = piglet;
owl.east = christopher;
christopher.south = pooh;
christopher.west = owl;
christopher.east = rabbit;
christopher.north = kanga;
rabbit.south = bees;
rabbit.west = christopher;
rabbit.east = gopher;
gopher.west = rabbit;
kanga.south = christopher;
kanga.north = eeyore;
eeyore.south = kanga;
eeyore.east = heffalumps;
heffalumps.west = eeyore;


tigger.greet = function(){console.log("The wonderful thing about Tiggers is Tiggers are wonderful things!");}
pooh.greet = function(){console.log("Oh bother");}
piglet.greet = function(){console.log("Oh d-d-d-d-dear! I wasn't expecting company");}
bees.greet = function(){console.log("Bzzzz");}
owl.greet = function(){console.log("What a hoot!");}
christopher.greet = function(){console.log("Hi there");}
rabbit.greet = function(){console.log("Get off my lawn");}
gopher.greet = function(){console.log("Wanna help me destroy Rabbit's lawn?");}
kanga.greet = function(){console.log("Have you seen Roo?");}
eeyore.greet = function(){console.log("[disgruntled emo noises]");}
heffalumps.greet = function(){console.log("What even is a heffalump?");}

var player = {
    location: tigger,
	hasHoney: false
}
function move(direction){
	if (direction in player.location){
		player.location = player.location[direction];
		console.log("You are now at " + player.location["character"] + "'s house");
		player.location.greet();
	}
	else{
		console.log ("You may not go that way!");
	}
}

function pickUp(){
	if (player.location == bees){
		if (player.hasHoney == false){
			console.log("You picked up the honey!");
			player.hasHoney = true;
		}
		else{
			console.log("You already have honey!");
		}
	}
	else{
		console.log("There isn't any honey here!");
	}
}

function drop(){
	if (player.hasHoney == false){
		console.log("You don't have any honey!");
	}
	else{
		if (player.location == pooh){
			console.log("Congratulations! You helped further Pooh's honey addiction!");
			player.hasHoney = false;
		}
		else{
			console.log("This isn't the location to deliver the honey!");
		}
	}
}

tigger.greet();