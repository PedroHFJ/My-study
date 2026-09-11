package Aulas.Teste;

import Aulas.Dominio.impressoraEstudante;
import Aulas.Dominio.Estudante02;

public class estudanteTeste02 {
    public static void main(String[]args){

        Estudante02 aluno01 = new Estudante02();
        Estudante02 aluno02 = new Estudante02();
        impressoraEstudante imprimir = new impressoraEstudante();

        aluno01.name = "Pedro";
        aluno01.age = 18;
        aluno01.sexo = 'M';

        aluno02.name = "Tamires";
        aluno02.age = 36;
        aluno02.sexo = 'F';

        imprimir.imprime(aluno01);
        System.out.println("-------------------------");
        imprimir.imprime(aluno02);

    }
}
