#include<iostream>
#include<windows.h>
int num, somando;
void soma();

int main(){
    SetConsoleOutputCP(CP_UTF8);
    std::cout<<"Digite um número: ";
    std::cin>>num;

    soma();
}

void soma(){
    for(int i = 0; i <= num; i++){
        somando += i;
    }
    std::cout<<"Número final é "<<somando;
}