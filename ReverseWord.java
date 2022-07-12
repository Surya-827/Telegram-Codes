import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;


public class Test{
	
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		String st = sc.next();
		String words[] = st.split("\\s");
		
		String rev = "";
		
		for(String s: words) {
			StringBuilder sb = new StringBuilder(s);
			rev+=sb.toString()+" "+rev;
			
		}
		System.out.println(rev);
	}
}
