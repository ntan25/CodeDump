import java.util.Scanner;
import java.util.Collections;
import java.util.List;
import java.util.ArrayList;


public class MinAndMaxInputChallenge {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        List list = new ArrayList();
        while(true){
            System.out.println("Enter a Number:");

            boolean isInt = scanner.hasNextInt();
            if(isInt){
                int num = scanner.nextInt();
                list.add(num);
                scanner.nextLine();
            }else{
                break;
            }


        }
        Collections.sort(list);
        System.out.println("Min Number: " + list.get(0));
        System.out.println("Max Number: " + list.get(list.size() - 1));
        scanner.close();
    }

}
