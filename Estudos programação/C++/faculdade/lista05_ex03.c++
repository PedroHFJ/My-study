#include <iostream>

int main(){
    const int n = 8;
    float array[n];
    bool jaContado[n] = {false};

    for(int i = 0; i < n; i++){
        std::cout << "Digite um número: ";
        std::cin >> array[i];
    }

    for(int i = 0; i < n; i++){
        if(jaContado[i]) continue;

        int contador = 1;

        for(int j = i + 1; j < n; j++){
            if(array[j] == array[i]){
                contador++;
                jaContado[j] = true;
            }
        }

        std::string vezes = (contador == 1) ? "vez" : "vezes";
        std::cout << array[i] << " ocorre " << contador << " " << vezes << std::endl;
    }

    return 0;
}