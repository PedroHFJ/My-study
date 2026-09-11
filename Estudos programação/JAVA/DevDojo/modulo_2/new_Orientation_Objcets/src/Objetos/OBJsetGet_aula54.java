package Objetos;

public class OBJsetGet_aula54 {
    private String nome;
    private int idade;

    public void setNome(String nome){
        this.nome = nome;
    }
    public String getNome(){
        return this.nome;
    }

    public void setIdade(int idade){
        if(idade < 0){
            return;
        }
        this.idade = idade;
    }
    public int getIdade(){
        return this.idade;
    }
}
