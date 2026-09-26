#include<iostream>
#include<windows.h>

int num1, num2;

void adicao();
void subtracao();
void resto();

int main(){
    SetConsoleOutputCP(CP_UTF8);

    std::cout<<"Digite o primeiro número:"<<std::endl;
    std::cin>>num1;

    std::cout<<"Digite o segundo número: "<<std::endl;
    std::cin>>num2;

    adicao();
    subtracao();
    resto();
}

void adicao(){
    int soma;
    soma = num1 + num2;
    std::cout<<"Adição: "<<std::endl;
    std::cout<<soma<<std::endl;
}

void subtracao(){
    int sub;
    sub = num1 - num2;
    std::cout<<"Subtração: "<<std::endl;
    std::cout<<sub<<std::endl;
}

void resto(){
    int resto;
    resto = num1 % num2;
    std::cout<<"Resto: "<<std::endl;
    std::cout<<resto;

}
