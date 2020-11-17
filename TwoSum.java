// nums = [2, 7, 11, 15], target = 9
// output = [0, 1] bc vals at 2 and 7 equal 9

import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;


public class TwoSum {





    public static void main(String[] args) {
        List<Integer> list = new ArrayList<>(Arrays.asList(2, 7, 11, 15));


        System.out.println("Input: " + list);
        System.out.println("Output: " + TwoSumSolver(list, 9));
    }
    public static List TwoSumSolver(List list, int target){
        List<Integer> output_list = new ArrayList<>();

        for (int i = 0; i <= list.size() - 1; i++ ){
            int val = (int) list.get(i);
            for (int j = i+1; j <= list.size() - 1; j++ ){
                int val2 = (int)list.get(j);
                if (val + val2 == target){
                    output_list.add(i);
                    output_list.add(j);

                }

            }

        }
        return output_list;

    }
}
