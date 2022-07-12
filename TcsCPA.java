

JAVA 1st Code 

import java.util.*;

public class MyClass {

 public static void main(String args[])

 {

  Scanner s=new 

Scanner(System.in);

  int n=s.nextInt();

  int r=0;

  if(n%2==0)

  {

   System.out.print("Cannot reverse");

  }

  else

  {

   while(n != 0)   

   {  

   int remainder = n % 10;  

 

    r = r * 10 + remainder;  

   n = n/10;  

   }  

   System.out.println(r);  

//ALLCODING1

  }

 }

}





JAVA FIRST CODE
