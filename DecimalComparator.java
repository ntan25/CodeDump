public class DecimalComparator {
    public static boolean areEqualByThreeDecimalPlaces (double firstint, double secondint) {
           firstint *= 1000;
           secondint *= 1000;
           firstint = (int)firstint;
           secondint = (int)secondint;
           if (firstint == secondint) {
               return true;
           } else {
               return false;
           }


    }
}
