#include<iostream>
#include<windows.h>

int matriz[3][3];
int num;
int linhas = sizeof(matriz)/sizeof(matriz[0]);
int colunas = sizeof(matriz[0])/sizeof(matriz[0][0]);
void carregarMatriz();
void verificarMatriz();


int main(){
    SetConsoleOutputCP(CP_UTF8);

    carregarMatriz();
    verificarMatriz();
}

void carregarMatriz(){
    for(int i=0;i<linhas;i++){
        for(int j = 0; j <colunas;j++){
            std::cin>>num;
            matriz[i][j] = num;
        }
    }
}

void verificarMatriz(){
    int repetidos[9];
    int quantidade = 0;

    for(int i = 0; i < linhas; i++){
        for(int j = 0; j < colunas; j++){

            bool jaFoiEncontrado = false;

            for(int k = 0; k < quantidade; k++){
                if(repetidos[k] == matriz[i][j]){
                    jaFoiEncontrado = true;
                    break;
                }
            }

            if(jaFoiEncontrado){
                continue;
            }

            int contador = 0;
            for(int x = 0; x < 3; x++){
                for(int y = 0; y < 3; y++){

                    if(matriz[x][y] == matriz[i][j]){
                        contador++;
                    }

                }
            }

            if(contador > 1){
                repetidos[quantidade] = matriz[i][j];
                quantidade++;
            }
        }
    }

    if(quantidade == 0){
        std::cout << "\nNao existem elementos repetidos.\n";
    }
    else{
        std::cout << "\nExistem " << quantidade << " elementos repetidos:\n";

        for(int i = 0; i < quantidade; i++){
            std::cout << repetidos[i] << " ";
        }

        std::cout << "\n";
    }
}
