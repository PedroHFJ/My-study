#include <iostream> 
using namespace std; 

void recebe(float cel);
void conversao();
float temperatura;
float tempNova;

int main(){
    int i;
    cout<<"Digite a temperatura: "<<endl;
    cin>>i;
    recebe(i);
    conversao();
}

void recebe(float cel){
    temperatura = cel;
}

void conversao(){
    tempNova = (temperatura*9/5)+32;
    cout<<temperatura<<"°C fica "<<tempNova<<"°F";
}