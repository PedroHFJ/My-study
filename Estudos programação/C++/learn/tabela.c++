#include<stdio.h>
#include<windows.h>


int main(){
    int opcao;
    float vlDeposito,  vlSaque, saldo=0;

    do{
        system("cls");
        printf("1-Depositar\n");
        printf("2-Sacar\n");
        printf("3-Exibir saldo\n");
        printf("4-Sair\n");
        printf("5-Escolha uma opcao: ");
        scanf("%i", &opcao);

        switch(opcao){
            case 1: 
                printf("Digite o valor do deposito: ");
                scanf("%f", &vlDeposito);
                saldo += vlDeposito;
                break;

            case 2:
                printf("Digite o valor do saque: ");
                scanf("%f", &vlSaque);
                if(vlSaque <= saldo){
                    printf("Saque realizado!");
                    saldo -= vlSaque;
                }else{
                    printf("Saque não realizado!\n");
                    printf("Saldo insuficiente!\n");
                }
                system("pause");
                break;

            case 3:
                printf("Seu saldo: R$%.2f\n", saldo);
                system("pause");
                break;
            case 4:
                printf("Fim do programa!\n");
                break;

        }

    }while(opcao!=4);
}
