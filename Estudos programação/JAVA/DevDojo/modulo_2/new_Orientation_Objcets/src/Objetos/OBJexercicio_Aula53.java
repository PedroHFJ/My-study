package Objetos;

import java.util.Scanner;

public class OBJexercicio_Aula53 {
    Scanner obj = new Scanner(System.in);

    public String nome;
    public int idade;
    public double [] salario;

    public void dados(){
        System.out.println("Digite o nome do funcionario: ");
        this.nome = obj.nextLine();

        System.out.println("Digite a idade do funcionario: ");
        this.idade = obj.nextInt();

        this.salario = new double [] {1500,1800,3000};
    }

    public void imprimeDados(){
        if(salario == null){
            return;
        }
        System.out.println("Nome: "+this.nome);
        System.out.println("Idade: "+this.idade);

        int salarioTotal = 0;
        int i = 0;
        for(double conta : this.salario){
            salarioTotal += conta;
            i +=1;
        }

        int media = salarioTotal/i;
        System.out.println("Média salarial: R$"+media);

    }

}
