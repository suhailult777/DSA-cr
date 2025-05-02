import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        // ArrayList<String> arraylist = new ArrayList<String>();

        DynamicArray dynamicArray = new DynamicArray(5);

        dynamicArray.add("A");
        dynamicArray.add("B");
        dynamicArray.add("C");
        dynamicArray.add("D");
        // growing the capacity
        dynamicArray.add("E");
        dynamicArray.add("F");

        // decreasing the capacity
        dynamicArray.delete("A");
        dynamicArray.delete("B");
        dynamicArray.delete("C");

        // dynamicArray.insert(0, "X");
        // dynamicArray.delete("A");
        // System.out.println("index of C: " + dynamicArray.search("C"));

        System.out.println(dynamicArray);
        System.out.println("size: " + dynamicArray.size);
        System.out.println("capacity: " + dynamicArray.capacity);
        System.out.println("empty: " + dynamicArray.isEmpty());
        System.out.println(dynamicArray.get(0));
    }
}
