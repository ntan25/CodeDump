public class NumberToWords {

    public static String numberToWords(int num){

        if (num < 0){
            return "Invalid Value";
        }


        int digits = 0;
        StringBuilder string = new StringBuilder();
        while (num != 0){
            digits = num % 10;
            switch(digits){
                case(1):
                    string.append("One ");
                    break;
                case(2):
                    string.append("Two ");
                    break;
                case(3):
                    string.append("Three ");
                    break;
                case(4):
                    string.append("Four ");
                    break;
                case(5):
                    string.append("Five ");
                    break;
                case(6):
                    string.append("Six ");
                    break;
                case(7):
                    string.append("Seven ");
                    break;
                case(8):
                    string.append("Eight ");
                    break;
                case(9):
                    string.append("Nine ");
                    break;
                default:
                    string.append("Zero ");
                    break;
            }
            num /= 10;

        }
        String newString = string.toString();
        return newString;

    }
}
