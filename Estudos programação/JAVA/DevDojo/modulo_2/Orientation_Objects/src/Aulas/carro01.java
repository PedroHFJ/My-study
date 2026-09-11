package Aulas;
import Aulas.Dominio.carros;

public class carro01 {
    public static void main(String[]args){
        carros cars = new carros();
        carros cars1 = new carros();

        cars.name = "Camaro";
        cars.modelo = "Chevrolet";
        cars.ano = 2020;

        System.out.println("Carro: "+cars.name+" Modelo: "+cars.modelo+" Ano: "+cars.ano);

        cars1.name = "Ferrari Enzo";
        cars1.modelo = "Ferrari";
        cars1.ano = 1980;

        System.out.println("Carro: "+cars1.name+" /Modelo: "+cars1.modelo+" /Ano: "+cars1 .ano);

    }
}
