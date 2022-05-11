public class DNA {
  public static void main(String[] args) {
    String dna1 = "ATGCGATACGCTTGA";
    String dna2 = "ATGCGATACGTGA";
    String dna3 = "ATTAATATGTACTGA";

    String dna = dna3;

    int dnaLength = dna.length();
    int start = dna.indexOf("ATG");
    System.out.println("Start is: " + start);

    int stop = dna.indexOf("TGA");
    System.out.println("End is: " + stop);

    if (start != -1 && stop != -1 && (start - stop) % 3 == 0) {
      System.out.println("Valid DNA");
      String protein = dna.substring(start, stop+3);
    }
    else {
      System.out.println("Not a protein");
    }

  }
}