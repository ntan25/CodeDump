import java.util.Collections;
import java.util.List;
import java.util.ArrayList;

public class LargetPrime {


    public static void main(String[] args) {
        System.out.println(getLargetPrime(21));
    }


    public static int getLargetPrime (int number){
        List<Integer> list = new ArrayList<>();
        for (int i = 1; i <= number; i++  ){
            if (number % i == 0){
                list.add(i);
            }
            else{
                continue;
            }
        }
        List<Integer> newlist = new ArrayList<>();

        for (int i = 0; i <= list.size() -1; i ++){
            int num = list.get(i);
            if (isPrime(num)){
                newlist.add(num);
            }
        }
        Collections.sort(newlist);
        return newlist.get(newlist.size() - 1);


    }

    public static boolean isPrime (int num){
        for (int i = 2; i<= num /2; i ++){
            if (num % i == 0){
                return false;

            }
        }return true;
        }
    }

