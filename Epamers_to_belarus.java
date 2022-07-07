
//Java 

import java.util.*;

public class Main

{

    static int[] par;

 public static void main(String[] args)

 { 

  Scanner sc=new Scanner(System.in);

  int n=sc.nextInt();

  int k=sc.nextInt();

  par=new int[n];

  for(int i=0;i<n;i++)

  {

      par[i]=i;

  }

  for(int i=0;i<k;i++)

  {

      int a=find(sc.nextInt());

      int b=find(sc.nextInt());

      if(a!=b)

          union(a,b);

  }

  Arrays.sort(par);

  int cnt=1;

  int pre=-1;

  int s=1;

  for(int i:par)

  {

      if(pre==-1)

      {

          pre=i;

      }

      else if(pre==i)

      {

          cnt++;

      }

      else{

          s=cnt;

          cnt=1;

          pre=i;

      }

  }

  System.out.println(cnt*s);

  

 }

 static int find(int ele)

 {

     if(par[ele]==ele) return ele;

     return par[ele]=find(par[ele]);

 }

 static void union(int a,int b)

 {

     if(a<b)

     {

         par[b]=a;

     }

     else

         par[a]=b;

 }

}

