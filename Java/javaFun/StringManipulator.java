public class StringManipulator {
    public String StringManipulator(String string) {
		return "test";
    }
	public String trimAndConcat(String first, String second){
		first = first.trim();
		second = second.trim();
		String result = first + second;
		return result;
	}
	public Integer getIndexOrNull(String string, char target){
		Integer result = string.indexOf(target);
		if (result == -1){
			result = null;
		}
		return result;
	}
	public Integer getIndexOrNull(String string, String target){
		Integer result = string.indexOf(target);
		if (result == -1){
			result = null;
		}
		return result;
	}
	
	public String concatSubstring(String first, int start, int end, String second){
		if (start <= first.length() -1 && end <= first.length()){
			String result = "";
			for (int i = start; i < end; i++){
				result = result + first.charAt(i);
			}
			result = result + second;
			return result;
		}
		else{
			return "index out of range yo";
		}
	}
}
