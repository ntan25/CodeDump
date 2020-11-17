public class FirstLastDigitSum {

    public static int sumFirstAndLastDigit (int number){
        if (number < 0){
            return -1;
        }

        int first_number = Integer.parseInt(Integer.toString(number).substring(0,1));
        int val = (Integer.toString(number)).length();
        int last_number = Integer.parseInt(Integer.toString(number).substring(val - 1,val ));
        return first_number + last_number;
    }
}
