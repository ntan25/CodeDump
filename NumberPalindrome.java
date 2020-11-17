public class NumberPalindrome {
    public static void main(String[] args) {
        System.out.println(isPalindrome(121));
    }
    public static boolean isPalindrome(int number){
        int abs_number = Math.abs(number);
        int new_number = Math.abs(number);
        int reverse = 0;
        while (new_number != 0){
            int digit = new_number % 10;
            reverse = reverse * 10 + digit;
            new_number /= 10;

        } 


        return number == reverse;
        }


    }

