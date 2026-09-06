#include<iostream>
#include<windows.h>
#include<random>


int main(){
    SetConsoleOutputCP(CP_UTF8);

    int numUser;
    int tentativas = 0;

    std::random_device rd;
    std::mt19937 gen(rd());

    std::uniform_int_distribution<> dist(1,50);
    int numMaq = dist(gen);

    std::cout<<"JOGO DE ADIVINHAÇÃO"<<std::endl;

    do{
        std::cout<<"\nDigite um número: ";
        std::cin>>numUser;
        tentativas += 1;

        if(numUser> numMaq){
            std::cout<<"Número é menor!"<<std::endl;
        }
        else if(numUser<numMaq){
            std::cout<<"Número é maior!"<<std::endl;
        }

    }while(numMaq!=numUser);
    std::cout<<"Parabéns você acertou!!!"<<std::endl;
    std::cout<<"Seu número de tentativas foi: "<<tentativas;

    return 0;
}