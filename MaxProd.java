import java.util.ArrayList;
import java.util.List;

public class MaxProd {

    int[] input = {1, 2, 3};

    // int[] input = {-2, -1, 1, 2, 3};

    public static void main(String[] args) {
        MaxProd m = new MaxProd();
        List<Integer> ll =  m.max(0);
        for (int i : ll) {
            System.out.println(i);
        }
        ll.sort((x,y) -> Integer.compare(x, y));
        System.out.println("The max: " + ll.get(ll.size() -1 ));

    }

    private List<Integer> max(int index) {
        if (index < input.length){
            List<Integer> l = new ArrayList<>();
            List<Integer> retList = max(index + 1);

            for (int j : retList){
                l.add(input[index] * j);
            }
            l.add(input[index]);
            l.addAll(retList);
            return l;
        }
        else return new ArrayList<>();

    }
}
