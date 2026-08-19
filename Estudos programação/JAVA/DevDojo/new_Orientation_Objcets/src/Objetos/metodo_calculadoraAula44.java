package Objetos;
import java.util.Scanner;

public class metodo_calculadoraAula44 {

    public void somar(){
        Scanner obj = new Scanner(System.in);

        System.out.println("Escolha o primeiro número: ");
        int a = obj.nextInt();

        System.out.println("Escolha o segundo número: ");
        int b = obj.nextInt();

        System.out.println(a+b);
        System.out.println(a-b);
        System.out.println(a*b);
    }

    public void calcular(int a, int b){
        System.out.println(a+b);
    }
}
