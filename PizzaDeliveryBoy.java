/* package codechef; // don't place package name! */

import java.util.*;

import java.lang.*;

import java.io.*;

class Tips implements Comparable<Tips>{

    private int andy;

    private int bob;

    private int diff;

    Tips(int andy, int bob, int diff) {

        this.andy = andy;

        this.bob = bob;

        this.diff = diff;

    }

    public int getAndy() {

        return this.andy;

    }

    public int getBob() {

        return this.bob;

    }

    public int getDiff() {

        return this.diff;

    }

    public int compareTo(Tips tip) {

        return tip.diff - this.diff;

    }

}

class Codechef

{

    public static void main (String[] args) throws java.lang.Exception

    {

        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        int x = sc.nextInt();

        int y = sc.nextInt();

        List<Tips> tips = new ArrayList<>();

        int[] andy = new int[n];

        for(int i=0; i<n; i++)

            andy[i] = sc.nextInt();

        int[] bob = new int[n];

        for(int i=0; i<n; i++) {

            bob[i] = sc.nextInt();

            tips.add(new Tips(andy[i], bob[i], Math.abs(andy[i]-bob[i])));

        }

        Collections.sort(tips);

        int total = 0;

        Iterator<Tips> itr = tips.iterator();

        while(itr.hasNext()) {

            Tips tip = itr.next();

            if(tip.getAndy() > tip.getBob() && x>0) {

                total += tip.getAndy();

                x--;

            }

            else {

                total += tip.getBob();

                y--;

            }

        }

    

        System.out.println(total);

    }

}
