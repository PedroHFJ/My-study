#include<iostream>
#include<windows.h>


int main(){
    SetConsoleOutputCP(CP_UTF8);
    int num;
    int soma = 0;
    do{
        std::cout<<"Digite um número pra somar: ";
        std::cout<<"Digite zero caso queira sair"<<std::endl;
        std::cin>>num;
        soma +=num;

    }while(num!=0);
    std::cout<<"A soma desses numeros é igual a "<<soma<<std::endl;
}