#include<iostream>
#include<windows.h>

using namespace std;

int main(){
    SetConsoleOutputCP(CP_UTF8);

    int nota1, nota2;
    float media;

    std::cout<<"Digite a nota da primeira prova: ";
    std::cin>>nota1;

    std::cout<<"\nDigite a nota da segunda prova: ";
    std::cin>>nota2;

    media = (nota1 + nota2)/2;

    if(media == 10){
        cout<<"Sua nota "<<media<<" foi excelente";
    }
    else if(media >= 9 || media<10){
        cout<<"Sua nota "<<media<<"  foi muito boa";
    }
    else if(media >= 7 || media <9){
        cout<<"Sua nota "<<media<<" foi boa";
    }
    else if(media >=6 || media <7){
        cout<<"Sua nota "<<media<<" foi regular";
    }
    else if(media<6){
        cout<<"Sua nota "<<media<<" foi insuficiente";
    }
    
}