#include<iostream>
#include<windows.h>

int main(){
    SetConsoleOutputCP(CP_UTF8);

    int pares, num = 0;
    int array[6];
    
    while(num<=6){
        std::cout<<"Digite um número par: ";
        std::cin>>pares;

        if(pares%2 == 1){
            std::cout<<"O número digitado não é par"<<std::endl;
        }
        array[num] = pares;
        num+=1;
    }

    num = 6;
    while(num>=0){
        std::cout<<array[num]<<", ";
        num -= 1;
    }
}