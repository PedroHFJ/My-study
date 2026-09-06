#include<iostream>
using namespace std;

int main(){
    int num;
    int soma = 0;
    do{
        cout<<"Digite zero caso queira sair"<<endl;
        cout<<"Digite um numero pra somar: ";
        cin>>num;
        soma +=num;

    }while(num!=0);
    cout<<"A soma desses numeros = "<<soma<<endl;
}