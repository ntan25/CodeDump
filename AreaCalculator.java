public class AreaCalculator {

    public static double area (double radius){
        if (radius >= 0){
            double area = (Math.pow(radius, 2)) * Math.PI;
            return area;
        } else {
            return -1;
        }



    }

    public static double area(double x, double y){
        if (x >= 0 && y >= 0) {
            double area = x * y;
            return area;
        } else {
            return -1;
        }
    }




}
