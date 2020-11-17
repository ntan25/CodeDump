import org.w3c.dom.ls.LSOutput;

public class MegaBytesConverter {


    public static void printMegaBytesAndKiloBytes(int kiloBytes) {
        if (kiloBytes < 0) {
            System.out.println("Invalid Value");
        }else {
            int newMegaByte  = kiloBytes / 1024;
            int newKiloByte = kiloBytes % 1024;
            System.out.println(kiloBytes + " KB = " + newMegaByte + " MB and " + newKiloByte + " KB" );
        }

    }


}