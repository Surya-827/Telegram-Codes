import java.util.Scanner;


public class Test{
	
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		String s = sc.nextLine();
		solve(s);
	}
	
	public static boolean Check(String str) {
		
		boolean flag = str.matches("[a-zA-Z]+");
		return flag;
	}
		
	public static void solve(String str) {
		
		boolean ans = Check(str);
		String result = ans==true ? "France" : "Italy";
		
		System.out.println(result);
	}
	
}

