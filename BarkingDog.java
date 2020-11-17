public class BarkingDog {

    public static boolean shouldWakeUp(boolean barking, int time) {
        if (time < 0 || time > 24) {
            return false;
        } else {
            return (time < 8 || time > 22) && barking;


        }
    }
}

