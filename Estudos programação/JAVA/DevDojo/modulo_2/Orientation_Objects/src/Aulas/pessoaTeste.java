package Aulas;
import Aulas.Dominio.Estudante;

public class pessoaTeste {
    public static void main(String[]args){
        Estudante estudante = new Estudante ();


        estudante.age = 18;
        estudante.nome = "João";
        estudante.sex = 'M';

        System.out.println();

        System.out.println(estudante.age);
        System.out.println(estudante.sex);

    }
}
