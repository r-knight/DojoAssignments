//accrues $107,374,182.40 after 30 days
//takes 17 days to reach 10000
//takes 34 days to reach 1000000000
//takes 1028 days to reach "Infinity"

function for30days(){
	var value = 0.1;
	for (var i = 0; i < 30; i++){
		value *=2;
	}

	console.log(value + " accrued after 30 days.");
}

function for10k(){
	var value = 0.1;
	var days = 0;
	for (var i = 0; value < 10000; i++){
		value *=2;
		days = days+1;
	}
	console.log(days + " days to reach 10000 dollars.");
}

function for1B(){
	var value = 0.1;
	var days = 0;
	for (var i = 0; value < 1e9; i++){
		value *=2;
		days++;
	}
	console.log(days + " days to reach 1 billion dollars.");
}

function toInfinity(){
	var value = 0.1;
	var days = 0;
	for (var i = 0; value < Infinity; i++){
		value *=2;
		days++;
	}
	console.log(days + " days to reach Infinity");
}

function forXDays(num){
	var value = 0.1;
	var days = 0;
	for (var i = 0; i<num; i++){
		value *=2;
		days++;
	}
	console.log(value + " accrued after " + days +" days.");
}
function forXAmount(amount){
	var value = 0.1;
	var days = 0;
	for (var i = 0; value < amount; i++){
		value *=2;
		days++;
	}
	console.log(days + " days to accrue " + amount +" dollars.");
	
}

for30days(); //accrues $107,374,182.40 after 30 days
for10k(); //takes 17 days to reach 10000
for1B(); //takes 34 days to reach 1000000000
toInfinity(); //takes 1029 days to reach "Infinity"
forXDays(16);
forXDays(17);
forXDays(33);
forXDays(34);
forXAmount(1e9);
forXDays(1027);
forXDays(1028);
forXAmount(Infinity);