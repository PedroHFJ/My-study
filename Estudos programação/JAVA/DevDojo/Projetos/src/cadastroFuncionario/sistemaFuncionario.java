package cadastroFuncionario;

import java.util.Scanner;

public class sistemaFuncionario {
    public static void main(String[]args){
        Scanner obj = new Scanner(System.in);
        funcionarios pessoas = new funcionarios();
        int opcao;
        int id= 0;

        do{

            System.out.println("======Sistema de Funcionarios======");
            System.out.println("1-Adicionar funcionario");
            System.out.println("2-Excluir funcionarios");
            System.out.println("3-Exibir funcionario");
            System.out.println("4-Sair");
            System.out.println("==================================");
            System.out.println();
            System.out.printf("Escolha uma opção: ");
            opcao = obj.nextInt();

            switch(opcao){
                case 1:
                    System.out.println("Digite o nome do funcionario: ");
                    obj.nextLine();
                    String nome = obj.nextLine();
                    pessoas.nome.add(nome);

                    System.out.println("Digite o salario do funcionario: ");
                    String salario = obj.nextLine();
                    pessoas.salario.add(salario);

                    System.out.println("Digite a idade do funcionario: ");
                    String idade = obj.nextLine();
                    pessoas.idade.add(idade);


                    String ti = Integer.toString(id);
                    pessoas.id.add(ti);
                    id +=1;
                    break;

                case 2:
                    System.out.println("Digite o id do funcionario que você deseja excluir: ");
                    obj.nextLine();
                    String idFun = obj.nextLine();

                    int index = pessoas.id.indexOf(idFun);

                    if(index != -1){
                        System.out.println("Usuário encontrado!");
                        System.out.println();

                        pessoas.nome.remove(index);
                        pessoas.idade.remove(index);
                        pessoas.salario.remove(index);
                        pessoas.id.remove(index);
                    }else{
                        System.out.println("Usuário não encontrado");
                    }
                    break;

                case 3:
                    System.out.println("======Funcionarios da empresa======");
                    int tamanho = pessoas.id.size();
                    for(int i = 0; i < tamanho; i++){
                        System.out.println("Id: "+pessoas.id.get(i));
                        System.out.println("Nome: "+pessoas.nome.get(i));
                        System.out.println("Salario: R$"+pessoas.salario.get(i)+",00");
                        System.out.println("Idade: "+pessoas.idade.get(i));
                        System.out.println("===================================");
                    }
                    break;

                case 4:
                    System.out.println("Finalizado");
                    break;

                default:
                    System.out.println("Opção invalida");
            }
        }while(opcao!=4);

        obj.close();
    }
}
