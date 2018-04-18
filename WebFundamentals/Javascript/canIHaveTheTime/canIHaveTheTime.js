function printTime(HOUR, MINUTE, PERIOD)
{
	var when = "";
	var morningOrEvening = "";
	var noon = false;
	if (PERIOD =="AM")
	{
		if (HOUR == 12){
			morningOrEvening = "at night.";
		}
		else{
			morningOrEvening = "in the morning.";
		}
	}
	else{
		if (HOUR == 12){}
			{
				morningOrEvening = ".";
				noon=true;
			}
		}
		else if (HOUR <=4){
			morningOrEvening = "in the afternoon.";					
		}
		else if (HOUR <=9)
		{
			morningOrEvening = "in the evening.";
		}
		else{
			morningOrEvening = "at night.";
		}
	}
	
	if(MINUTE < 30){
		
		if(MINUTE == 15){
			when = "a quarter after";
		}
		else if (MINUTE == 5){
			when = "5 after";
		}
		else{
			when = "just after";
		}
		
		if(!noon){
			when += " " + HOUR;
		}
	}
	else if (MINUTE > 30){
		
		if (HOUR == 11 && PERIOD == "AM"){
			noon = true;
			morningOrEvening = ".";
		}
		
		if(MINUTE == 45){
			when = "a quarter til";
		}
		else if (MINUTE == 55){
			when = "5 til";
		}
		else{
			when = "almost";
		}
		
		if (HOUR+1 <=4){
			morningOrEvening = "in the afternoon.";					
		}
		else if (HOUR+1 <=9)
		{
			morningOrEvening = "in the evening.";
		}
		else{
			morningOrEvening = "at night.";
		}
		
		if(!noon)
		{
			if (HOUR == 11){
				morningOrEvening = "at night.";
			}
			when += " " + (HOUR+1);
		}
	}
	else{
		if(HOUR == 12 && PERIOD === "PM"){
			when = "half past"
			noon = true;
		}
		else
		{
			when = "half past " + HOUR;
			if (HOUR == 12){
				morningOrEvening = "at night.";
			}
		}
	}
	if (!noon){
		console.log("It's", when, morningOrEvening);
	}
	else{
		console.log("It's", when, "noon");
	}
}
printTime(8, 30, "AM");
printTime(12, 45, "PM");
printTime(12, 30, "AM");
printTime(4, 45, "PM");
printTime(3, 25, "PM");
printTime(11, 45, "AM");