import java.util.Scanner;

public class ReverseArray {

    public static int[] reverseArray(int[] inputArray) {
        // Create a new array to store the reversed elements
        int[] reversedArray = new int[inputArray.length];

        // Loop through the input array from the end to the beginning
        for (int i = 0; i < inputArray.length; i++) {
            reversedArray[i] = inputArray[inputArray.length - 1 - i];
        }

        return reversedArray;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Prompt user for array size
        System.out.print("Enter the number of elements in the array: ");
        int n = scanner.nextInt();

        // Initialize the input array
        int[] array = new int[n];

        // Take array elements as input
        System.out.println("Enter the elements of the array:");
        for (int i = 0; i < n; i++) {
            array[i] = scanner.nextInt();
        }

        // Reverse the array
        int[] reversed = reverseArray(array);

        // Print the reversed array
        System.out.println("Reversed Array:");
        for (int num : reversed) {
            System.out.print(num + " ");
        }

        scanner.close();
    }
}
