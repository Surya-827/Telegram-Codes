public class SmithNumbers {

   public static boolean isPrime(int number) {

      int loop;

      int prime = 1;

      for(loop = 2; loop < number; loop++) {

         if((number % loop) == 0) {

            prime = 0;

         }

      }

      if (prime == 1) {

         return true;

      } else {

         return false;

      }

   }

   public static ArrayList<Integer> primeFactors(int number) {

      int sum = 0;

      ArrayList al = new ArrayList();

      for(int i = 2; i< number; i++) {

         while(number % i == 0) {

            System.out.println(i+" ");

            al.add(i);

            number = number/i;

         }

      }

      if(number >2) {

         System.out.println(number);

         al.add(number);

      }

      return al;

   }

   public static void main(String args[]) {

      Scanner sc = new Scanner(System.in);

      System.out.println("Enter a number :");

      int num = sc.nextInt();

      int sum = 0;

     

      if(isPrime(num)) {

         System.out.println("Given number is not smith number ");

      } else {

         ArrayList<Integer> arrayList = primeFactors(num);

         System.out.println("Prime factors of the given number are"+arrayList);

         Iterator it = arrayList.iterator();

         

         while(it.hasNext()) {

            int n = (int) it.next();

            System.out.println(n);

            while(n!=0) {

               sum = sum+n%10;

               n = n/10;

            }

         }

         int temp = 0;

         while(num != 0) {

            temp = temp + num%10;

            num = num/10;

         }

         System.out.println("sum of the digits of the numbers of the prime factorization: "+sum);

         System.out.println("Sum of digits in the given number: "+temp);

         

         if(temp==sum) {

            System.out.println("Given number is a smith number");

         } else {

            System.out.println("Given number is not smith number ");

         }

      }

   }

}





