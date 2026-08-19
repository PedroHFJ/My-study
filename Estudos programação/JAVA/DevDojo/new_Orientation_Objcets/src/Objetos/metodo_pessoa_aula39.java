package Objetos;
import Objetos.pessoa_aula39;
import java.util.Scanner;

public class metodo_pessoa_aula39 {
    pessoa_aula39 pessoa = new pessoa_aula39();
    Scanner obj = new Scanner(System.in);
    public void imprime(){

        System.out.println("Qual o seu nome? ");
        String nome = obj.nextLine();
        pessoa.nome = nome;

        System.out.println("Qual a sua idade? ");
        int idade = obj.nextInt();
        pessoa.idade = idade;

        System.out.println("Qual o seu sexo(F/M)? ");
        char sexo = obj.next().charAt(0);
        pessoa.sexo = sexo;

        System.out.println("Nome: "+pessoa.nome);
        System.out.println("Idade: "+pessoa.idade);
        System.out.println("Sexo: "+pessoa.sexo);
    }
}
