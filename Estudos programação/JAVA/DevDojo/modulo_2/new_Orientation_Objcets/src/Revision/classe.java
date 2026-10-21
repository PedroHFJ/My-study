package Revision;
import java.util.Scanner;

public class classe {
    private String name;
    private int age;
    private int cpf;
    private double salary;

    public void setName(String name){
        this.name = name;
    }
    public String getName(){
        return name;
    }

    public void setAge(int age){
        if (age < 0){
            throw new IllegalArgumentException("Idade invalida");
        }
        this.age = age;
    }
    public int getAge(){
        return age;
    }

    public void setCpf(int cpf){
        this.cpf = cpf;
    }
    public int getCpf(){
        return cpf;
    }

    public void setSalary(double salary){
        if (salary < 0){
            throw new IllegalArgumentException("Salario invalido");
        }
        this.salary = salary;
    }
    public double getSalary(){
        return salary;
    }


    public void registrar(){
        Scanner obj = new Scanner(System.in);

        System.out.println("Digite o nome do funcionario:");
        this.name = obj.nextLine();

        System.out.println("Digite a idade do funcinario: ");
        setAge(this.age = obj.nextInt());

        System.out.println("Digite o cpf do funcionario: ");
        this.cpf = obj.nextInt();

        System.out.println("Digite o salario do funcionario: ");
        setSalary(this.salary = obj.nextDouble());

        obj.close();
    }

    public void imprimir(){
        System.out.println(this.name);
        System.out.println(this.age);
        System.out.println(this.cpf);
        System.out.println(this.salary);
    }
}
