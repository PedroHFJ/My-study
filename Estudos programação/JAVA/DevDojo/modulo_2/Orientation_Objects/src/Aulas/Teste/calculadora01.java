package Aulas.Teste;
import Aulas.Dominio.calculadora;

public class calculadora01 {
    public  static void main(String[]args) {
        calculadora Calcular = new calculadora();

        Calcular.soma();

        Calcular.division();

        Calcular.multi(40,20);

        double resultado = Calcular.dividi(40,10);
        System.out.println(resultado);

        Calcular.retorno(60,0);
    }
}
