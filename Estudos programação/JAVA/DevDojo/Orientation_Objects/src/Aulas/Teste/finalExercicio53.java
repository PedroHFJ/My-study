package Aulas.Teste;
import Aulas.Teste.exercicio53Metodo;
import Aulas.Dominio.exercicio53;

import java.util.Scanner;

public class finalExercicio53 {
    public static void main(String[]args) {

        Scanner usuario = new Scanner(System.in);
        exercicio53Metodo metodo = new exercicio53Metodo();

        System.out.println("Quantos funcionários você quer cadastrar? ");
        int qtdFun = usuario.nextInt();

        exercicio53[] funcionarios = new exercicio53[qtdFun];
        double mediaSalarial = 0;

        for (int i = 0; i < qtdFun; i++) {
            exercicio53 fun = new exercicio53();

            usuario.nextLine();

            System.out.println("Nome do funcionário: ");
            fun.nome = usuario.nextLine();

            System.out.println("CPF do funcionário: ");
            fun.CPF = usuario.nextLong();

            System.out.println("Idade do funcionário: ");
            fun.idade = usuario.nextInt();

            usuario.nextLine();

            System.out.println("GMAIL do funcionário: ");
            fun.GMAIL = usuario.nextLine();

            System.out.println("Salário do funcionário: ");
            fun.salario = usuario.nextDouble();

            funcionarios[i] = fun;
            mediaSalarial += fun.salario;


        }
        System.out.println("======CADASTRO======");
        for (int i = 0; i < qtdFun; i++){
            metodo.dados(funcionarios[i]);
        }
        double total = mediaSalarial/qtdFun;
        System.out.println("A media Salarial da empresa é R$"+total);

        usuario.close();

    }
}
