import java.util.Collections;
import java.util.List;
import java.util.ArrayList;

public class GreatestCommonDivisor<i> {


    public static int getGreatestCommonDivisor(int num1, int num2){
        if (num1 < 10 || num2 < 10){
            return -1;
        }
        int val = 0;
         if (num1 < num2){
             val = num1;
         }else {
             val = num2;
         }
         List<Integer> list = new ArrayList<>();
        for (int i = 1; i <= val; i++){

            if (num1 % i == 0 && num2 % i == 0){
                list.add(i);

            }
        }

        Collections.sort(list);
        return list.get(list.size() - 1);
    }
    }
