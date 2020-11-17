import java.util.List;
import java.util.ArrayList;

public class FactorPrinter {



    public static void printFactors(int num){
        if (num < 1){
            System.out.println("Invalid Value");
        }
        List<Integer> list = new ArrayList<>();
        for (int i = 1; i <= num; i ++ ){
            if (num % i == 0){
                list.add(i);
            }

        }

        System.out.println(list);
    }
}
