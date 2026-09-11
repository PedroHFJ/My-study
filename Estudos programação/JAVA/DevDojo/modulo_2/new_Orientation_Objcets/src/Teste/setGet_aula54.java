package Teste;

import Objetos.OBJsetGet_aula54;

public class setGet_aula54 {
    public static void main(String[]args){
        OBJsetGet_aula54 pessoa = new OBJsetGet_aula54();

        pessoa.setNome("Pedro");
        pessoa.setIdade(18);
        System.out.println(pessoa.getNome());
        System.out.println(pessoa.getIdade());
    }
}
