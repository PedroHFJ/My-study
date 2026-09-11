package Aulas;
import Aulas.Dominio.Professor;

public class professor01 {
    public static void main(String[]args) {
        Professor prof = new Professor();

        prof.name = "Goku";
        prof.age = 18;
        prof.sexo = 'M';

        System.out.println(prof.name+" "+prof.sexo+" "+prof.age);
    }
}
