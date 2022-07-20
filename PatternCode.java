import java.util.*;
import java.io.*;

public class Main {
  
    public static void myCode(String str){
    
        int num = Integer.parseInt(str);
      
        for(int i=1;i<=num;i++){
            for(int j=num-1;j>=i;j--){
                System.out.println(" ");
            }
            for(int k=1;k<=2*i-1;k++){
                System.out.println("*");
            }
            for(int l=num-1;l>=i;l--){
                System.out.println(" ");
            }
            System.out.println();
        }
      
    }
  
    public static void main(String[] SURYA){
    
        Scanner sc = new Scanner(System.in);
        String st = sc.next();
        myCode(st);
      
    }

}
