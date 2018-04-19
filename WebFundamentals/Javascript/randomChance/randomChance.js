function randomChance(quarters, optsTarget)
{
	
	var target = -1;
	if (optsTarget != undefined){
		if (optsTarget > 0){
			target = optsTarget;
		}
	}
	var wallet = quarters;
	while (wallet > 0){
		wallet--;
		var spin = Math.trunc(Math.random()*100)+1;
		if (spin == 100){
			console.log(wallet);
			var winnings = Math.trunc(Math.random()*51)+50;
			console.log(winnings);
			wallet += winnings;
			if (wallet >= target){
				return wallet;
			}
			else{
				console.log("Not enough winnings, continuing to play");
			}
		}
	}
	
	return 0;
}