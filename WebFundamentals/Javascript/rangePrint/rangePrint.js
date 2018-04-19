function printRange(arg1, arg2, arg3)
{
	var start = 0;
	var end = 0;
	var step = 0;
	if (arg3 != undefined){
		step = arg3;
	}
	else
	{
		step = 1;
	}
	if (arg2 != undefined){
		start = arg1;
		end = arg2;
	}
	else{
		end = arg1;
	}
	
	if (step == 0 || (step < 0 && start < end)){
		console.log("Invalid input");
		return;
	}
	for (var i = start; i < end; i += step)
	{
		console.log(i);
	}
}
printRange(2,10,2);
printRange(4,8);
printRange(4);
printRange(-2,10,2);
printRange(2,10,-2);