package Teste;

import Objetos.OBJsetGet_aula55;

public class setGet_aula55 {
    public static void main(String[]args){
        OBJsetGet_aula55 pessoa = new OBJsetGet_aula55();

        pessoa.setNome("Pedro");
        pessoa.setIdade(18);
        pessoa.setCpf(1112223);
        pessoa.setSalario(new double[]{123,213,433});


        pessoa.imprime();
    }
}
