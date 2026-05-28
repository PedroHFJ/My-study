package introduçãoORBJ.dominio.teste;
import java.util.Scanner;
import introduçãoORBJ.dominio.pessoa;

public class testandoPessoa {
    public static void main(String[] args) {
        Scanner obj = new Scanner (System.in);
        pessoa estudante = new pessoa();

        estudante.sexo = 'M';

        System.out.println("Digite seu nome: ");
        estudante.name = obj.nextLine();

        System.out.println("Digite sua idade: ");
        estudante.age = obj.nextInt();


        System.out.println(estudante.age);
        System.out.println(estudante.sexo);
        System.out.println(estudante.name);
    }
}
