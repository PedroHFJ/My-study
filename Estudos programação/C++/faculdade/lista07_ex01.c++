#include<iostream>
#include<windows.h>

int A[4][3];
int B[4][3];
int C[4][3];

void carregarMatriz();
void somarMatriz();
void mostrarMatrizes();
int linhas = sizeof(A)/sizeof(A[0]);
int colunas = sizeof(A[0])/sizeof(A[0][0]);



int soma=0, num;

int main(){
    SetConsoleOutputCP(CP_UTF8);

    carregarMatriz();
    somarMatriz();
    mostrarMatrizes();

    return 0 ; 
}

void carregarMatriz(){

    std::cout<<"Array A: "<<std::endl;
    for(int i = 0; i < linhas; i++){
        for(int j = 0; j< colunas; j++){
            std::cout<<"Digite os números do Array A: ";
            std::cin>>num;
            A[i][j] = num;
        }
    }

    std::cout<<"\nArray B: "<<std::endl;
    for (int i = 0; i < linhas; i++){
        for(int j= 0; j< colunas;j++){
            std::cout<<"Digite os número do Array B: ";
            std::cin>>num;
            B[i][j] = num;
        }
    }
    std::cout<<std::endl;

}


void somarMatriz(){
    for(int i=0; i<linhas; i++){
        for(int j=0;j<colunas;j++){
            soma = A[i][j] + B[i][j];
            C[i][j] = soma;
           
        }
    }

    std::cout<<"Soma dos arrays: "<<soma;
    std::cout<<std::endl;
}

void mostrarMatrizes(){
    std::cout<<"\nArray A: "<<std::endl;
    for(int i=0; i <linhas; i++){
        for (int j=0; j <colunas;j++){
  
            std::cout<<A[i][j]<<" ";
        }
        std::cout<<"\n";
    }
    std::cout<<std::endl;

    std::cout<<"\nArray B: "<<std::endl;
    for(int i=0; i <linhas; i++){
        for (int j=0; j <colunas;j++){
  
            std::cout<<B[i][j]<<" ";
        }
        std::cout<<"\n";
    }

    std::cout<<std::endl;


    std::cout<<"\nArray C: "<<std::endl;
    for(int i=0; i <linhas; i++){
        for (int j=0; j <colunas;j++){
  
            std::cout<<C[i][j]<<" ";
        }
        std::cout<<"\n";
    }

}