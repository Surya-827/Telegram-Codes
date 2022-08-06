import java.util.*; 
 
class Test{ 
  
    public String getComplex(int x,int y,String op){ 
       if(op.equals("-"){ 
         return String.format("%d%s%dj",x,y,op);
       }
       return "Not Valid";
    }
} 
public static Main{ 
  public static void main(String[] args){ 
    Scanner sc = new Scanner(System.in);
    int x = sc.nextInt();
    int y = sc.nextInt();
    String op = sc.next();
    Test t = new Test();
    System.out.print(t.getComplex(x,y,op));
    
  }
}
