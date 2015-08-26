/******************************************************************************
 *  Compilation:  javac Hi.java
 *  Execution:    java Hi yourname
 *
 *  Prints "Hi, Bob. How are you?" where "Bob" is replaced by the
 *  command-line parameter.
 *
 *  % java Hi Bob
 *  Hi, Bob. How are you?
 *
 *  % java Hi Alice
 *  Hi, Alice. How are you?
 *
 ******************************************************************************/

public class Hi {

    public static void main(String[] args) {
        System.out.print("Hi, ");
        System.out.print(args[0]);
        System.out.println(". How are you?");
    }

}

