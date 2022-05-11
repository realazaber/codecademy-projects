import java.util.ArrayList;

class Playlist {
  
  public static void main(String[] args) {
    ArrayList<String> desertIslandPlaylist = new ArrayList<String>();

    desertIslandPlaylist.add("Funny Song");
    desertIslandPlaylist.add("Sad song");
    desertIslandPlaylist.add("Happy song");
    desertIslandPlaylist.add("Cheeky song");
    desertIslandPlaylist.add("Meme song");

    System.out.println(desertIslandPlaylist);

    int a = desertIslandPlaylist.indexOf("Sad song");
    int b = desertIslandPlaylist.indexOf("Meme song");

    System.out.println(a);
    System.out.println(b);

    String tempA = "Sad song";
    String tempB = "Meme song";
    desertIslandPlaylist.set(b, tempA);
    desertIslandPlaylist.set(a, tempB);

    System.out.println(desertIslandPlaylist);  
  }
}