package Objetos;

public class OBJsetGet_aula55 {
    private String nome;
    private int idade;
    private int cpf;
    private double [] salario;


    public String getNome() {
        return this.nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public int getCpf() {
        return this.cpf;
    }

    public void setCpf(int cpf) {
        this.cpf = cpf;
    }

    public int getIdade() {
        return this.idade;
    }

    public void setIdade(int idade) {
        this.idade = idade;
    }

    public double[] getSalario() {
        return this.salario;
    }

    public void setSalario(double[] salario) {
        this.salario = salario;
    }


    public void imprime(){
        System.out.println(getNome());
        System.out.println(getCpf());
        System.out.println(getIdade());
        for(double a : this.salario){
            System.out.println(a);
        }
    }
}
