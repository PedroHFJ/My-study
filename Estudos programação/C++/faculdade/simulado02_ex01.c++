#include<iostream>

int main(){
    int array [4] = {3,5,2,8};
    int total = 0;

    for(int i = 0; i < 4; i++){
        if (array[i] % 2 ==0){
            total += array[i];
        }
        else{ total += 1;}
    }

    std::cout<<"Total = "<<total;
    return 0;
}