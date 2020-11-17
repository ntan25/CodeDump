public class SharedDigit {


    public static void main(String[] args) {
        System.out.println(hasSharedDigit(19,99));
    }



    public static boolean hasSharedDigit (int num1, int num2){
        if (num1 < 10 || num1 > 99 || num2 < 10 || num2 > 99 ){
            return false;
        }

        int left1 = num1/10;
        int right1 = num1 % 10;
        int left2 = num2/10;
        int right2 = num2 % 10;
        return(left1 == left2 || left1 == right2 || right1 == left2 || right1 == right2);
    }
}
