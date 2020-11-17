import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class ThreeSum {


    public static void main(String[] args) {
        List<Integer> list = new ArrayList<>(Arrays.asList(2, 7, 0, 15));


        System.out.println("Input: " + list);
        System.out.println("Output: " + ThreeSumSolver(list, 9));
    }
    public static List ThreeSumSolver(List list, int target){
        List<Integer> output_list = new ArrayList<>();

        for (int i = 0; i <= list.size() - 1; i++ ){
            int val = (int) list.get(i);
            for (int j = i+1; j <= list.size() - 1; j++ ){
                int val2 = (int)list.get(j);
                for (int k = i + 2; k<= list.size()-1; k++){
                    int val3 = (int)list.get(k);
                    if (val + val2 + val3 == target){
                        output_list.add(i);
                        output_list.add(j);
                        output_list.add(k);
                }


                }

            }

        }
        return output_list;

    }
}
