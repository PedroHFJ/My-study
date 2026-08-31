package Teste;

import java.util.Scanner;
import Objetos.MetodoReferencia_aula49;
import Objetos.estudante_aula49;

public class estudanteTeste_aula49 {
    public static void main(String[]args){

        Scanner obj = new Scanner(System.in);
        MetodoReferencia_aula49 imprime = new MetodoReferencia_aula49();

        estudante_aula49 estudante1 = new estudante_aula49();
        estudante_aula49 estudante2 = new estudante_aula49();

        System.out.println("Digite os dados da primeira pessoa: ");

        System.out.println("Digite seu nome: ");
        String nome1 = obj.nextLine();

        System.out.println("Digite sua idade: ");
        int idade1 = obj.nextInt();

        System.out.println("Digite seu sexo: ");
        char sexo1 = obj.next().charAt(0);

        System.out.println();

        System.out.println("Digite os dados da segunda pessoa: ");

        String nome3 = obj.nextLine();

        System.out.println("Digite seu nome: ");
        String nome2 = obj.nextLine();

        System.out.println("Digite sua idade: ");
        int idade2 = obj.nextInt();

        System.out.println("Digite seu sexo: ");
        char sexo2 = obj.next().charAt(0);

        estudante1.nome = nome1;
        estudante1.idade = idade1;
        estudante1.sexo = sexo1;

        estudante2.nome = nome2;
        estudante2.idade = idade2;
        estudante2.sexo = sexo2;

        imprime.inserindoDados(estudante1);

        imprime.inserindoDados(estudante2);

        obj.close();

    }
}
