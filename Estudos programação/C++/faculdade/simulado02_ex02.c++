#include<iostream>

int matriz[3][2], total = 0;
void carregarMatriz();
void mostrarMatriz();
void somaElemento();



int main(){

    carregarMatriz();
    mostrarMatriz();
    somaElemento();

}

void carregarMatriz(){
    for(int i = 0; i < 3; i++){
        for (int j = 0; j < 2; j ++){
            std::cout<<"\nDigite o numero para a matriz: "<<std::endl;
            std::cin>>matriz[i][j];
        }
    }
}

void mostrarMatriz(){
    for(int i = 0; i< 3; i++){
        for (int j =0; j < 2; j++){
            std::cout<<matriz[i][j]<<", ";
        }
    }
}

void somaElemento(){
    for (int i = 0; i < 3; i++){
        for(int j = 0; j < 2; j++){
            total += matriz[i][j];
        }
    }
    std::cout<<"\nTotal: "<<total;
}