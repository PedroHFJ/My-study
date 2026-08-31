package Objetos;

public class somaDeArray_Aula52 {
    public void soma(int [] numeros){
        int a = 0;
        for(int num : numeros){
            a += num;
        }
        System.out.println(a);
    }
}
