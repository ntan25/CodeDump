public class Wall {

    private double width;
    private double height;

    public double getWidth() {
        return width;
    }

    public void setWidth(double width) {
        if (width >= 0){
            this.width = width;
        }
        else{
            this.width = 0;
        }
    }

    public double getHeight() {
        return height;
    }

    public void setHeight(double height) {
        if (height < 0){
            this.height = 0;
        }
        else {
            this.height = height;
        }
    }

    public double area(){
        return height * width;
    }
}
