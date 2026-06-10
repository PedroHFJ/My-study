public class variosMetodos {
    public void calculateArea(int x){
        int resultado = x*x;
        System.out.println("Square area with side 5: "+resultado);
    }
    public void calculateArea(int weight, int leght){
        int resultado = weight*leght;
        System.out.println("Rectangle area with length 4 and width 6: "+resultado);
    }

    public void calculateArea(double radius){
        double resultado = radius*radius*3.14;
        System.out.println("Circle area with radius 2.5: "+resultado);
    }

    public static void main(String[] args) {
        variosMetodos area = new variosMetodos();

        area.calculateArea(5);          // square
        area.calculateArea(4, 6);       // rectangle
        area.calculateArea(2.5);        // circle
    }
}


