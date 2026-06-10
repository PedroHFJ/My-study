import java.util.Scanner;

public class Methods {
    public static void mult(int a, int b){
        System.out.println(a*b);
    }
    public static void main(String[]args){
        try(Scanner obj = new Scanner(System.in)) {

            System.out.println("Escolha o valor de a: ");
            int a = obj.nextInt();

            System.out.println("Escolha o valor de b: ");
            int b = obj.nextInt();
            mult(a,b);
        }

    }
}
