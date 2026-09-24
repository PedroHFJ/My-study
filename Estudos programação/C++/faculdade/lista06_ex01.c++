#include <iostream> 
using namespace std; 

void recebe(int x);
void fatorial();
int num;

int main(){
    
    recebe(6);
    fatorial();
    return 0;
}

void recebe(int x){
    num = x;
}

void fatorial(){
    int resultado = 1;

    cout<<"O fatorial de "<<num<<endl;
    if(num == 0){
        num = 1;
        cout<<"É igual a "<<num;
    }
    else if(num < 0){
        cout<<"Essa conta não existe";
    }
    else if(num >= 1){
        for(int i = 1; i <=num;i++){
            resultado = resultado*i;
        }
        cout<<"É igual a "<<resultado;
    }
}

