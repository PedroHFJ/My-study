package Aulas;
import Aulas.Dominio.calculadora;
import org.w3c.dom.ls.LSOutput;

public class calculadora01 {
    public  static void main(String[]args) {
        calculadora soma = new  calculadora();

        soma.somaDoisNumeros();
        System.out.println("Fazendo metodos");

        soma.multiplicação(10,20);
    }
}
