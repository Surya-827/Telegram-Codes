import java.util.*;

class Solution{
    
    public int[] getSeries(int n) {
        
        int[] arr = new int[n+1];
        
        for(int i=0;i<n+1;i++){
            int f = ((5*i)+2);
            
            if(f%4!=0){
                arr[i] = f;    
            }
            else{
                continue;
            }
        }
        
        return arr;
    }
    
}

public class Main{
    public static void main(String[] args){
        
        Scanner sc = new Scanner(System.in);
        Solution s = new Solution();
        
        int n = sc.nextInt();
        int[] arr = s.getSeries(n);
        
        for(int i:arr){
            if(i!=0){
                System.out.println(i);
            }
        }
    }
}
