"""

The following code adds two positive integers without using the '+' operator.

The code uses bitwise operations to add two numbers.

Input: 2 3

Output: 5

"""

public class Main{ 

    public static void main(String[] args){ 

        Scanner sc = new Scanner(System.in);

        int x = sc.nextInt();

        int y = sc.nextInt();

        

        while(y){ 

            int carry = x & y;

            x = x^y;

            y = carry <<1;

        }

        System.out.print(x);

    }

}
