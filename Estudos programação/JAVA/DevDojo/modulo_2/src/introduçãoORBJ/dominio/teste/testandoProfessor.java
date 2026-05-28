package introduçãoORBJ.dominio.teste;
import introduçãoORBJ.dominio.professor;
public class testandoProfessor {
    public static void main(String[]args) {
        professor prof = new professor();
        prof.name = "Pedro";
        prof.sexo = 'M';
        prof.age = 29;

        System.out.println(prof.name + " " + prof.age + " " + prof.sexo);
    }
}
