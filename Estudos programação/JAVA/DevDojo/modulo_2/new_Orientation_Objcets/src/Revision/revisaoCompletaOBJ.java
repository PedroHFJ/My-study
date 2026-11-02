package Revision;

import java.util.Scanner;

public class revisaoCompletaOBJ {
    private String nome;
    private String idade;
    String [] funNome = new String [100];
    String [] funIdade = new String [100];
    int qtd
= 0;

    public void setNome(String nome){
        this.nome = nome;
    }
    public String getNome(){
        return this.nome;
    }

    public void setIdade(String idade){
        this.idade = idade;
    }

    public String getIdade(){
        return this.idade;
    }


    public void BdFuncionarios() {
        Scanner obj = new Scanner(System.in);
        int  op = 0;


        do{
            System.out.println();
            System.out.println("======CADASTRO DE FUNCIONARIO======");
            System.out.println("1-Cadastrar funcionarios");
            System.out.println("2-Ver funcionarios");
            System.out.println("3-Sair");
            System.out.println("===================================");
            System.out.println();
            System.out.println("Escolha uma opção: ");
            op = obj.nextInt();
            obj.nextLine();

            switch(op){
                case 1:

                    System.out.println("Digite o nome do funcionario");
                    this.nome = obj.nextLine();
                    funNome[qtd] = this.nome;

                    System.out.println("Digite a idade do funcionario");
                    this.idade = obj.nextLine();
                    funIdade[qtd] = this.idade;

                    qtd += 1;

                    break;

                case 2:
                    if (qtd ==0){
                        System.out.println("Nenhum funcionario cadastrado");
                    }
                    for(int p = 0; p < qtd; p++){
                        System.out.println("Nome: "+funNome[p]);
                        System.out.println("Idade :"+funIdade[p]);
                        System.out.println();

                    }
                    break;
                case 3:
                    System.out.println("Obrigado!!!");
                    break;

                default:
                    System.out.println("Opção inválida!");
            }

        }while(op != 3);

    }

}
