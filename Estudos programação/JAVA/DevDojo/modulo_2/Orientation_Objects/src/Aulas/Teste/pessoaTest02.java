package Aulas.Teste;
import Aulas.Dominio.pessoa;

public class pessoaTest02 {
    public static void main(String[]args){
        pessoa person = new pessoa();

        person.nome = "Pedro";
        person.idade = 18;

        person.setName("Julia Vianna");
        person.setAge(18);

        person.imprime();
        System.out.println("============");

        System.out.println(person.getName());
    }
}
