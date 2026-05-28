package introduçãoORBJ.dominio.teste;

import introduçãoORBJ.dominio.carro;

public class testandoCarro {
    public static void main(String[] args) {
        carro car = new carro();
        carro car2 = new carro();

        car.name =  "Camaro";
        car.modelo = "Chevrolet";
        car.age = 2019;

        car2.name = "Ferrari F50";
        car2.modelo = "Ferrari";
        car2.age = 1989;

        System.out.println("Nome do carro: " + car.name);
        System.out.println("Ano do carro: " + car.age);
        System.out.println("Modelo do carro: " + car.modelo);

        System.out.println("\nNome do carro: " + car2.name);
        System.out.println("Ano do carro: " + car2.age);
        System.out.println("Modelo do carro: " + car2.modelo);
    }
}
