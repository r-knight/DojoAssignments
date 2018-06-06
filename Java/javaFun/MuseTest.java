import java.util.ArrayList;
import java.util.HashMap;
public class MuseTest{
	public static void main(String[] args){
		
		HashMap<String, String> tracklist = new HashMap<String, String>();
		
		Muse muse = new Muse();

		tracklist.put("Map of the Problematique", "Fear, and panic in the air / I want to be free / From desolation and despair");
		tracklist.put("Newborn", "Link it to the world / Link it to yourself / Stretch it like a birth squeeze / The love for what you hide");
		tracklist.put("Knights of Cydonia", "No one's going to take me alive / Time has come to make things right / You and I must fight for our rights / You and I must fight to survive");
		tracklist.put("Hysteria ", "'Cause I want it now / I want it now / Give me your heart and your soul / And I'm breaking out / I'm breaking out / Last chance to lose control");

		System.out.println("******Getting song lyrics from 'Knights of Cydonia'*******");
		String songLyrics = tracklist.get("Knights of Cydonia");
		System.out.println(songLyrics);

		System.out.println("******Printing all track names and lyrics in the format 'Song title': 'Lyrics'*******");
		muse.printLyrics(tracklist);
	}

}