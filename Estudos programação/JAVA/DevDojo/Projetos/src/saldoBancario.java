import java.util.Scanner;

public class saldoBancario {
    public static void main(String[]args){
        Scanner obj = new Scanner(System.in);
        float saldo = 0;
        int opcao = 0;
        float vlDeposito = 0;
        float vlSaque = 0;

        System.out.println("Digite o seu nome: ");
        String nome = obj.nextLine();

        do{

            System.out.println("======CONTA BANCARIA======");
            System.out.println("1-Deposistar na conta");
            System.out.println("2-Sacar dinheiro da conta");
            System.out.println("3-Exibir saldo");
            System.out.println("4-Sair");
            System.out.println("==========================");

            System.out.println("Bem vindo a sua conta "+nome);

            System.out.println();

            System.out.println("Escolha uma opção: ");
            opcao = obj.nextInt();

            switch(opcao){
                case 1:
                    System.out.println("Digite o valor do deposito: ");
                    vlDeposito = obj.nextFloat();
                    saldo +=vlDeposito;
                    break;

                case 2:
                    System.out.println("Digite o valor do saque: ");
                    vlSaque = obj.nextFloat();

                    if (saldo >= vlSaque){
                        System.out.println("Saque realizado com sucesso!");
                        saldo -= vlSaque;
                    }else{
                        System.out.println("Saldo insuficiente");
                    }

                case 3:
                    System.out.println("Seu saldo "+nome);
                    System.out.println(saldo);
                    break;

                case 4:
                    System.out.println("Finalizamos por aqui "+nome+"!");
                    break;

            }
        }while(opcao!=4);
    }
}
