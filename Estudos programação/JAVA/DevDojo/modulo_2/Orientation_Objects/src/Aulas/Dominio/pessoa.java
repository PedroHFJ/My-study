package Aulas.Dominio;

public class pessoa {
    public String nome;
    public int idade;
    private String name;
    private int age;
    //Quando usamos private é como se o usuário não pudesse acessar esse atributo

    public void imprime(){
        System.out.println(this.nome);
        System.out.println(this.idade);

        System.out.println("============");

        System.out.println(this.name);
        System.out.println(this.age);
    }

    public void setName(String name){
        this.name = name;
    }
    public void setAge(int age){
        if (age < 1){
            System.out.println("Idade invalida");
            return;
        }
        this.age = age;
    }

    public String getName(){
        return "Sophia";
    }
}

