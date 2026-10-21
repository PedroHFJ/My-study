package Objetos;

public class Funcionarios01 {
    private String nome;
    private int idade;
    private double salary;


    public Funcionarios01(String nome, int idade, double salary){
        setNome(nome);
        setIdade(idade);
        setSalary(salary);
    }

    public Funcionarios01(){
    }

    public void setNome(String nome){
        if (nome == null || nome.isBlank()){
            throw new IllegalArgumentException("O nome não pode ser nulo");
        }
        this.nome = nome.trim();
    }

    public String getNome(){
        return nome;
    }

    public void setIdade(int idade){
        if (this.idade < 0){
            throw new IllegalArgumentException("Idade invalida");
        }
        this.idade = this.idade;
    }

    public int getIdade(){
        return idade;
    }

    public void setSalary(double salary){
        if(this.salary < 1100){
            throw new IllegalArgumentException("Salario invalido");
        }
        this.salary = this.salary;
    }

    public double getSalary(){
        return salary;
    }


    private void lerCampo()

}
