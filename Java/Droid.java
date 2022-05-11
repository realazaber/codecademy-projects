public class Droid {

  int batteryLevel;
  String name;

  public Droid(String droidName) {
    name = droidName;
    batteryLevel = 100;
  }

  public String toString() {
    return "Hello, I'm the droid: " + name;
  }

  public void performTask(String task) {
    System.out.println("Codey is performing task: " + task);
    batteryLevel -= 10;
  }

  public void energyReport() {
    System.out.println("Battery Level: " + batteryLevel);
  }

  public static void main(String[] args) {
    Droid Codey = new Droid("Codey");

    System.out.println(Codey);

    Codey.performTask("Jump");

    Codey.energyReport();

  }

}
