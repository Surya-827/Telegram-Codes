import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;


public class Test{
	
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		//Add Values in list to find maxPosPosition
		List<Integer> lst = new ArrayList<>();
		Collections.sort(lst,Collections.reverseOrder());
		long sum = lst.get(0);
		int count=0;
		
		if(lst.get(0)>0) {
			count++;
		}
		for(int i=1;i<lst.size();i++) {
			if(lst.get(i)+sum>0) {
				count++;
			}
			sum+=lst.get(i);
		}
		System.out.println(count);
	}
}
