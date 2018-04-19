function printArray(array, symbol, reversedOptional)
{
	var reverse = false;
	var bullet = "->";
	var start = 0;
	var end = array.length;
	var step = 1;
	
	if (reversedOptional != undefined){
		if (reversedOptional == true){
			reverse = true;
		}
		else
		{ // if 3rd arg is false or a non-bool value, treat reverse
			reverse = false;
		}
	}
	
	if(reverse == true){
		start = array.length-1;
		end =  0;
		step = -1;
	}
	if(symbol != undefined){
		bullet = symbol;
	}
	
	if (!reversedOptional){
		for (var i = start; i < end; i+=step){
			console.log(i,bullet,array[i]);
		}
	}
	else
	{
		for (var i = start; i >= end; i+=step){
			console.log(i,bullet,array[i]);
		}
	
	}
}

var testArray = [ "James", "Jill", "Jane", "Jack" ];
printArray(testArray);
printArray(testArray, "==>");
printArray(testArray, "~~>", true);
printArray(testArray, ">>>", false);
printArray(testArray, "-----", "q");