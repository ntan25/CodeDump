public class FlourPacker {

    public static void main(String[] args) {
        System.out.println(canPack(1, 0, 6));
    }

    public static boolean canPack(int bigCount, int smallCount, int goal){

        if (bigCount < 0 || smallCount < 0 || goal < 0) {
            return false;
        }
        bigCount *= 5;
        smallCount *= 1;
        return(bigCount + smallCount <= goal);
    }
}
