#include<iostream>
#include<windows.h>

int matriz[4][4];
int linhas = sizeof(matriz)/sizeof(matriz[0]);
int colunas = sizeof(matriz[0])/sizeof(matriz[0][0]);
void mostrarArray();

int main(){
    SetConsoleOutputCP(CP_UTF8);

    for(int i=0; i < linhas; i++){
        for(int j=0; j < colunas; j++){
            if(i == j){
                matriz[i][j] = 0;
            }
            else if(i > j){
                matriz[i][j] = i;
            }
            else if(i < j){
                matriz[i][j] = j;
            }
        }
    }

    mostrarArray();
}

void mostrarArray(){
    for(int i=0; i < linhas; i++){
        for(int j=0; j < colunas; j++){
            std::cout<<matriz[i][j]<<" ";
        }
        std::cout<<"\n";
    }
}