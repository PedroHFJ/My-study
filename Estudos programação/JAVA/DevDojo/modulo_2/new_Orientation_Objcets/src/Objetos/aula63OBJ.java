package Objetos;

public class aula63OBJ {
    private String nome;
    private static int[] episodios;

    static{
        System.out.println("Inicializando");
        episodios = new int [100];
        for(int i = 0; i < episodios.length; i++){
            episodios[i] = i+1;
        }
    }

    public void imprimir(){
        System.out.println("O bloco estatico faz sempre a inicialização primeiro ");
        System.out.println("Não dá para entrar em uma variavel nele");
        System.out.println();
        for(int i =0; i < episodios.length;i++){
            System.out.print(episodios[i]+", ");
        }
    }
}
