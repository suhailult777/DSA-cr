import java.util.*;

public class MainHash {
    public static void main(String[] args) {
        // inintially we have capacity of 11 and loadfactor 75 percent it will
        // dynamically change the capacity
        Hashtable<Integer, String> table = new Hashtable<Integer, String>(10);

        table.put(100, "spongbob");
        table.put(123, "patrick");
        table.put(321, "squidward");
        table.put(555, "sandy");
        table.put(777, "Gary");

        // removing the enteries
        // table.remove(777);

        for (Integer key : table.keySet()) {
            System.out.println(key.hashCode() % 10 + " " + key + " " + table.get(key));
        }

    }
}
