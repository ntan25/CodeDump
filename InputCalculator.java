import java.util.Scanner;

public class InputCalculator {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int counter = 0;
        int sum = 0;
        while(true){
            System.out.println("Enter Number: ");
            boolean isInt = scanner.hasNextInt();

            if(isInt){
                int num = scanner.nextInt();
                counter++;
                sum += num;

            }
            else{
//                System.out.println("SUM = " + sum + " AVG = " + (sum/counter));
                break;
            }
        }
        System.out.println("SUM = " + sum + " AVG = " + (sum/counter));


        scanner.close();

    }
}
