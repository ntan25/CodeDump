public class MinutesToYearsDayCalculator {

    public static void printYearsAndDays(long minutes){
        if (minutes >= 0){
            long years = minutes / 525600;
            long days = (minutes % 525600) / 1440;
            years = (int)years;
            days = (int)days;
            System.out.println(minutes + " min = " + years + " y and " + days + " days"  );
        }else {
            System.out.println("Invalid Value");
        }
    }
}
