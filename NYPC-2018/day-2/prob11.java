import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;
import java.util.Collections;
import java.util.Comparator;

public class Main {
    
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        int n = scn.nextInt();
        int m = scn.nextInt();
        List<Integer> infected = new ArrayList<Integer>();
        infected.add(1);
        List<ArrayList<Integer>> events = new ArrayList<ArrayList<Integer>>();
        for (int i = 0; i < m; i++) {
            List<Integer> tmp = new ArrayList<Integer>(); 
            tmp.add(scn.nextInt());
            tmp.add(scn.nextInt());
            tmp.add(scn.nextInt());      
            events.add((ArrayList<Integer>)tmp);      
        }
        Collections.sort(events, new ListComparator(2));
        // System.out.println(events.toString());
        for (ArrayList<Integer> e : events) {
            // System.out.println(e.toString());
            boolean inf_0 = infected.contains(e.get(0));
            boolean inf_1 = infected.contains(e.get(1));
            if (inf_0 && inf_1) {
                continue;
            }
            if (inf_0 && !inf_1) {
                infected.add(e.get(1));
            }
            if (inf_1 && !inf_0) {
                infected.add(e.get(0));
            }
        }
        Collections.sort(infected);
        infected.forEach(i -> System.out.print(i + " "));
        System.out.println();
    }

    // https://stackoverflow.com/questions/5335892/java-sort-list-containing-list-on-index-value-of-list#answer-5335908
    public static class ListComparator implements Comparator<List<Integer>> {
        private final int indexToCompare;

        public ListComparator(int indexToCompare) {
            this.indexToCompare = indexToCompare;
        }

        public int compare(List<Integer> first, List<Integer> second) {
            Integer firstValue = first.get(indexToCompare);
            Integer secondValue = second.get(indexToCompare);
            return firstValue.compareTo(secondValue);
        }
    }

}
