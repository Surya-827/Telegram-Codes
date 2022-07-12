import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;


public class Test{
	
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		String st = sc.next();
		Set<Character> s = new HashSet<>();
		
		for(char ch: st.toCharArray()) {
			s.add(ch);
			
		}
		if(st.equalsIgnoreCase(" ")) {System.out.println(-1);}
		else {
			System.out.println(s.size());
		}
	}
}
