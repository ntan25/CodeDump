import java.util.Scanner;

public class ReadingUserInputChallenge {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int count = 0;
        int sum = 0;
        while (count < 10){

            int order = count + 1;
            System.out.println("Enter number #" + order + ":");
            boolean isAnInt = scanner.hasNextInt();
            if (isAnInt){
                int num = scanner.nextInt();
                count++;
                sum += num;


            }
            else{
                System.out.println("Invalid Number");
            }
            scanner.nextLine(); // handle end of line (enter key)


            }
        System.out.println("Sum = " + sum);
        scanner.close();
        }

    }


