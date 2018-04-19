function numbersOnly(array){
	var numsOnly = [];
	if (array.length === 0){
		return;
	}
	
	for (var i = 0; i < array.length; i++){
		if(typeof(array[i]) == "number"){
			numsOnly.push(array[i]);
		}
	}

	return numsOnly;
}

function noNumbers(array){
	if (array.length === 0){
		return;
	}
	
	for (var i = array.length -1; i >=0; i--){
		if(typeof array[i] == "number"){
			array.splice(i,1);
		}
	}

}