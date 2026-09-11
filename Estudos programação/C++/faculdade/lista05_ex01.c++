#include<iostream>
#include<windows.h>

int main(){
    SetConsoleOutputCP(CP_UTF8);

    int num, num2;
    int array1[10], array2[10];
    int lenArray = sizeof(array1)/sizeof(array1[0]);
    
    for(int i = 0; i < lenArray; i++){
        std::cout<<"\nDigite o "<<i<<"° número "<<std::endl;
        std::cin>>num;

        array1[i] = num;
    }

    for(int i = 0; i < lenArray;i++){
        num2 = array1[i];
        num2 = num2*num2;

        array2[i] = num2;
    }

    for(int i = 0; i <lenArray;i++){
        std::cout<<"\n"<<array1[i]<<" ao quadrado é igual a "<<array2[i]<<std::endl;
    }

    return 0;
}


