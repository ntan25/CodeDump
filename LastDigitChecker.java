public class LastDigitChecker {




    private static int rightDigitExtracter(int num) {
        if (num >= 10 && num < 100) {
            return num % 10;
        } else if (num >= 100 && num < 999) {
            return num % 100;
        } else {
            return 0;
        }

    }

    public static boolean hasSameLastdigit(int num1, int num2, int num3) {
        if (num1 < 10 || num1 > 1000 || num2 < 10 || num2 > 1000 || num3 < 10 || num3 > 1000) {
            return false;
        }


        return ((rightDigitExtracter(num1) == rightDigitExtracter(num2)) ||
                (rightDigitExtracter(num1) == rightDigitExtracter(num3) ||
                        rightDigitExtracter(num2) == rightDigitExtracter(num3)));


    }
}
