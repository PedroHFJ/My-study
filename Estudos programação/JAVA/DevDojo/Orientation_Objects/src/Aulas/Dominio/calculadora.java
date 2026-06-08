package Aulas.Dominio;
import java.util.Scanner;
import java.util.Scanner;

public class calculadora {
    Scanner calcular = new Scanner(System.in);

    public void soma(){
        System.out.println(10+10);
    }
    //Isso é um def em JAVA

    public void division(){
        System.out.println("Primeiro número: ");
        int num1 = calcular.nextInt();

        System.out.println("Segundo número: ");
        int num2 = calcular.nextInt();

        float result = num1/num2;

        System.out.println("O resultado será: "+result);
    }

    public void multi(int x, int y){
        System.out.println(x*y);
    }

    public double dividi(double a, double b){
        if (a == 0 || b == 0){
            return 0;
        }else{
            return a/b; //Pode colocar só essa linha (tirando o "else")
        }
    }

    public void retorno(int w, int z){
        if(w == 0 || z == 0){
            System.out.println("Não exisiti divisão por zero");
            return;
        }
        System.out.println(w/z);
    }

    public void calculadora04(int num4, int num5){
        num4 =4;
        num5 = 5;
        System.out.println("num4 = "+num4);
        System.out.println("num5 = "+num5);
    }
}
