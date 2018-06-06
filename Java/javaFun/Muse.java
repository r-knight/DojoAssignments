import java.util.ArrayList;
import java.util.HashMap;
import java.util.Set;
public class Muse{

	public HashMap<String, String> generateHashMap (ArrayList<String> titles, ArrayList<String> lyrics)
	{
		//Zips songs and titles into a hash map
		HashMap<String, String> tracklist = new HashMap<String,String>();
		if (titles.size() != lyrics.size() || titles.size() == 0){
			return tracklist;
		}
		
		for (int i = 0; i < titles.size(); i ++){
			tracklist.put(titles.get(i), lyrics.get(i));
		}

		return tracklist;
	}
	public void printLyrics(HashMap<String, String> songs)
	{
		Set<String> keys = songs.keySet();
		for(String key : keys){
            System.out.println(key + ": " + songs.get(key)); 
		}
	}


}