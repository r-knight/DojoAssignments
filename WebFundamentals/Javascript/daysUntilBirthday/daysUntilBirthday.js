var daysUntilMyBirthday = 330;

var birthdayMessage =	'♪ღ♪*•.¸¸¸.•*¨¨*•.¸¸¸.•*•♪ღ♪¸.•*¨¨*•.¸¸¸.•*•♪ღ♪•*\n' +
						'♪ღ♪░H░A░P░P░Y░ B░I░R░T░H░D░A░Y░░♪ღ♪\n' +
						'*•♪ღ♪*•.¸¸¸.•*¨¨*•.¸¸¸.•*•♪¸.•*¨¨*•.¸¸¸.•*';
while (daysUntilMyBirthday > 0){
	if (daysUntilMyBirthday >= 30){
		console.log(daysUntilMyBirthday, "days until my birthday. Long way to go..");
	}
	else if(daysUntilMyBirthday < 30 && daysUntilMyBirthday >=5)
	{
		console.log(daysUntilMyBirthday, "days until my birthday!");
	}
	else{
		if (daysUntilMyBirthday >1){
			console.log(daysUntilMyBirthday, "DAYS UNTIL MY BIRTHDAY!!");
		}
		else if (daysUntilMyBirthday == 1){
			console.log(daysUntilMyBirthday, "DAY UNTIL MY BIRTHDAY!!");
		}
	}
	daysUntilMyBirthday--;
}

console.log(birthdayMessage);

/* FUNCTION VERSION

function daysUntilBirthday(num){
	var daysUntilMyBirthday = num;
	var birthdayMessage =	'♪ღ♪*•.¸¸¸.•*¨¨*•.¸¸¸.•*•♪ღ♪¸.•*¨¨*•.¸¸¸.•*•♪ღ♪•*\n' +
						'♪ღ♪░H░A░P░P░Y░ B░I░R░T░H░D░A░Y░░♪ღ♪\n' +
						'*•♪ღ♪*•.¸¸¸.•*¨¨*•.¸¸¸.•*•♪¸.•*¨¨*•.¸¸¸.•*';
	while (daysUntilMyBirthday > 0){
		if (daysUntilMyBirthday >= 30){
			console.log(daysUntilMyBirthday, "days until my birthday. Long way to go..");
		}
		else if(daysUntilMyBirthday < 30 && daysUntilMyBirthday >=5)
		{
			console.log(daysUntilMyBirthday, "days until my birthday!");
		}
		else{
			if (daysUntilMyBirthday >1){
				console.log(daysUntilMyBirthday, "DAYS UNTIL MY BIRTHDAY!!");
			}
			else if (daysUntilMyBirthday == 1){
				console.log(daysUntilMyBirthday, "DAY UNTIL MY BIRTHDAY!!");
			}
		}
		daysUntilMyBirthday--;
	}
	console.log(birthdayMessage);
}

daysUntilBirthday(3);
daysUntilBirthday(1);
daysUntilBirthday(17);
daysUntilBirthday(50);

*/