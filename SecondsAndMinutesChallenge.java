import org.w3c.dom.ls.LSOutput;

public class SecondsAndMinutesChallenge {

    public static String getDurationString(int minutes, int seconds){
        if (minutes >= 0 && seconds <= 59 && seconds >= 0){
            int totalseconds = minutes * 60 + seconds;
            int hours = totalseconds / 3600;
            int minute = (totalseconds % 3600) / 60;
            int second = totalseconds % 216000;
            System.out.println(hours + "h " + minute + "m " + second + "s");

        }else{
            System.out.println("Invalid Value");;
        }
        return "";
    }
    
    public static String getDurationString(int seconds) {
        if (seconds >= 0) {
            int hours = seconds / 3600;
            int minute = (seconds % 3600) / 60;
            int second = seconds % 216000;
            System.out.println(hours + "h " + minute + "m " + second + "s");
        }else {
            System.out.println("Invalid Value");
        }
        return "";
    }

}
