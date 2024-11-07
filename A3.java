import java.io.*;
import java.util.*;

class A3 {
    static {
        System.loadLibrary("A3"); // Load the native library
    }

    // Native method declarations
    private native int add(int a, int b);
    private native int sub(int a, int b);
    private native int mult(int a, int b);
    private native int div(int a, int b);

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a, b, ch;

        // Input values for a and b
        System.out.println("\nEnter value of a: ");
        a = sc.nextInt();
        System.out.println("\nEnter value of b: ");
        b = sc.nextInt();

        // Menu loop
        do {
            System.out.println("\nENTER YOUR CHOICE: ");
            System.out.println("1. Add");
            System.out.println("2. Subtract");
            System.out.println("3. Multiply");
            System.out.println("4. Divide");
            System.out.println("5. Exit");
            ch = sc.nextInt();
            A3 calculator = new A3(); // Create an instance of A3

            switch (ch) {
                case 1:
                    calculator.add(a, b);
                    break;
                case 2:
                    calculator.sub(a, b);
                    break;
                case 3:
                    calculator.mult(a, b);
                    break;
                case 4:
                    calculator.div(a, b);
                    break;
                case 5:
                    System.out.println("Exiting...");
                    break;
                default:
                    System.out.println("Your choice is wrong.");
            }
        } while (ch < 5);

        sc.close(); // Close the scanner
    }
}
