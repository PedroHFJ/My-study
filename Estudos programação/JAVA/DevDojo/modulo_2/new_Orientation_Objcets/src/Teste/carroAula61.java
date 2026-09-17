package Teste;

import Objetos.carroAula61OBJ;

public class carroAula61 {
    public static void main(String[]args) {
        carroAula61OBJ c1 = new carroAula61OBJ("BMW", 240);
        carroAula61OBJ c2 = new carroAula61OBJ("Mercedes",240);
        carroAula61OBJ c3 = new carroAula61OBJ("Ferrari", 320);

        carroAula61OBJ.velocidadeLimite = 180;

        c1.imprime();
        c2.imprime();
        c3.imprime();

    }
}
