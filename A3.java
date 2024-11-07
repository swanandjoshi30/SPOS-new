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




We're using Java for writing the main program.
To demonstrate Dynamic Linking Library (DLL) in Java, we'll be declaring functions in Java and implementing them in C (can be C/C++).
First, we create a Java program A3.java,
This is the main Java file containing function definition and the main function.
Functions (add, sub, mul, div) in A3 class in this file are native functions, meaning their body is written in C/C++ in a different file.
After creating this file, you need to compile it. To do so, run javac A3.java (assuming you're already in the directory that contains this file).
Now, we will generate the header file. For this, run javac -h . A3.java.
There will be a new file called A3.h in your current working directory,
This is the header file.
It contains signatures for native functions we created in the Java file.
Thus, there's no need to memorized boilerplate in A3.c since the functions defined in that file can be found in the header file. I have included the A3.h file in this folder for reference. Note that it is automatically generated.
Create a new A3.c file which is the C program file containing function definitions (for add, sub, mul, div)
Define all the functions (add, sub, mul, div)
Then, we have to compile the C program file, i.e. A3.c. For this, run gcc -shared -o libA3.so -fPIC -I"$JAVA_HOME/include" -I"$JAVA_HOME/include/linux" A3.c,
gcc -> GNU compiler for C program
-shared -> tells the compiler to create a shared file (.so) instead of a regular executable file
-o libA3.so -> tells the compiler to save the output to libA3.so file
fPIC -> stands for Position-Independent Code. Needed for creating shared libraries.
-I"$JAVA_HOME/include" and -I"$JAVA_HOME/include/linux" -> -I flag used for specifiying directories to include. Values in double quotes are directories
A3.c -> name of the C program file to compile
Lastly, run the program using java -Djava.library.path=. A3
java -> Loads Java Virtual Machine (JVM)
-Djava.library.path=. -> -D is used to set a system property. In this case, we’re setting the java.library.path (for .so or .dll files) property.
A3 -> name of the Java class containing the main method



Compile A3.java:
javac A3.java
Generate header file:
javac -h . A3.java
Compile C code:
gcc -shared -o libA3.so -fPIC -I"$JAVA_HOME/include" -I"$JAVA_HOME/include/linux" A3.c
Note

If you get an error saying "fatal error: jni.h: No such file or directory", this might be because you haven't set $JAVA_HOME environment variable. Usually JVM stuff is in /usr/lib/jvm/java-<version>-openjdk-amd64. To set JAVA_HOME environment variable, run: export $JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64 (for version 17, adjust for your version accordingly.)

Run program:
java -Djava.library.path=. A3