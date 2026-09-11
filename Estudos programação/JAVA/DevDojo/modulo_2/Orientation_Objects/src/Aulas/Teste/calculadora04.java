package Aulas.Teste;

import Aulas.Dominio.calculadora;

public class calculadora04 {
    public static void main(String[]args){
        calculadora calcular = new calculadora();

        int num4 = 40;
        int num5 = 50;

        calcular.calculadora04(num4, num5);

        System.out.println("num 4: "+num4);
        System.out.println("num 5: "+num5);

    }
}
