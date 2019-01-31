package taller2_ed2;

/**
 *
 * @author Juan Sebastián Pérez Salazar - Yhoan Alejandro Guzman Garcia
 */
public class Taller2_ED2 {

    public static void subSetComb(String chain){
        System.out.println("Ø");
        subSetCombAux("", chain);
    }
    
    public static void subSetCombAux(String getChain, String restChain){
        if (restChain.equals("")){
            System.out.println(getChain);
        }else{
            subSetCombAux(getChain+restChain.charAt(0), restChain.substring(1));
            subSetCombAux(getChain, restChain.substring(1));
        }
    }
    
    public static void subSetPerm(String chain){
        subSetPermAux("", chain);
    }
    
    public static void subSetPermAux(String prefix, String sufix){
        if(sufix.length()==0) {
            System.out.println(prefix);
            System.out.println(AdvancedEncryptionStandard.desencriptarArchivo(prefix));
        }
        else{
            for(int i=0; i<sufix.length(); i++ ){
                subSetPermAux(prefix+sufix.charAt(i),sufix.substring(0,i)+sufix.substring(i+1));
            }
        }
    }
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        //subSetComb("abc");
        subSetPerm("abcd");
    }
    
}
