import java.util.*;

//JAVA 
class Test{  
     public int getDigitCount(int[] A,int N){ 
         int ans = 0;
          for(int ele: A) { 
              ans+=(ele%10);
          }
          return ans;
     }
}

public class Main {
	public static void main(String[] args) {
		Test t = new Test();
		Scanner sc = new Scanner(System.in);
		int siz = sc.nextInt();
		for(int i=0;i<siz;i++){ 
		    A[i] = sc.nextInt();
		}
		System.out.println(t.getDigitCount(A,siz));
	}
}


//PYTHON
class Solution(object):
    @classmethod
    def getDigitCount(cls,A:List[int],N: int) -> int:
        return sum([ ele%10 for ele in A ])
        
