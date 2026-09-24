#include <iostream> 
using namespace std; 

void recebe(int x);
void parOuImpar();
void primo();

int num;
bool priminho = true;

int main(){
    recebe(8);
    parOuImpar();
    primo();
    
    return 0;
}

void recebe(int x){
    num = x;
}

void parOuImpar(){
    if(num == 0){
        cout<<"Número nulo"<<endl;
    }
    else if(num%2 == 0){
        cout<<"Número par"<<endl;
    }
    else{
        cout<<"Número ímpar"<<endl;
    }
}

void primo(){
    
    for(int i = 2; i <num;i++){
        if(num%i == 0){
            cout<<"Número não é primo";
            priminho = false;
            break;
        }
        else if(num == 0){
            cout<<"Número nulo"<<endl;
        }
    }
    if (priminho == true){
        cout<<"Número primo";
    }
}