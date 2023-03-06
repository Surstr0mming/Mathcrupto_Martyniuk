import java.util.Date;
import java.util.Scanner;

public class kritpo_method_2 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.print("Enter number of remainder and divider(There is only one number, because they are equal) ");
        int k = in.nextInt();
        //long start_md1 = 0;
        /*
        подумати за панель
        проблеми з кількікітю вводу
        */
        /*
        можна відмалювати тільки руезультат
        не всі і на кроці, а тільки деякі
         */

        /*
        перевірку на простоту накинути
         */
        long start = 0;
        if (k > 0) {
            long[] myArray_of_divider = new long[k];
            long[] myArray_of_remainder = new long[k];

            boolean true_or_false2 = true;
            boolean true_or_false3 = true;

            System.out.println("Enter numbers to code" + "\n" +
                    "b - is a remainder" + "\n" +
                    "p - ia a divider" + "\n" +
                    "b must be less then p and they both must be positive" +
                    "and dividers must be not equal.");

            //остача - remainder
            //модуль - divider

            long b, p;
            for (int i = 0; i < k; i++) {
                boolean true_or_false1 = true;
                System.out.print("b" + (i + 1) + " = ");
                b = in.nextInt();
                System.out.print("p" + (i + 1) + " = ");
                p = in.nextInt();
                while (true_or_false1) {
                    if (b > p | b == p | b < 0 | p < 0) {
                        System.out.println("U entered something wrong at this stage. Please try again.");
                        System.out.print("b" + (i + 1) + " = ");
                        b = in.nextInt();
                        System.out.print("p" + (i + 1) + " = ");
                        p = in.nextInt();
                    } else {
                        true_or_false1 = false;
                    }
                }
                myArray_of_divider[i] = p;
                myArray_of_remainder[i] = b;
            }

            while (true_or_false2) {
                boolean true_or_false4 = false;
                for (int i_1 = 0; i_1 < k - 1; i_1++) {
                    for (int i_2 = i_1 + 1; i_2 < k; i_2++) {
                        if (myArray_of_divider[i_1] == myArray_of_divider[i_2] & myArray_of_remainder[i_1] != myArray_of_remainder[i_2]) {
                            true_or_false4 = true;
                        }
                    }
                }
                if (true_or_false4 == true) {
                    System.out.println("There are same divider, but different reminder. " +
                            "This is mistake, so enter number of remainder and divider again with same conditions.");
                    for (int i = 0; i < k; i++) {
                        System.out.print("b" + (i + 1) + " = ");
                        b = in.nextInt();
                        System.out.print("p" + (i + 1) + " = ");
                        p = in.nextInt();
                        while (true_or_false3) {
                            if (b > p | b == p | b < 0 | p < 0) {
                                System.out.println("U entered something wrong at this stage. Please try again");
                                System.out.print("b" + (i + 1) + " = ");
                                b = in.nextInt();
                                System.out.print("p" + (i + 1) + " = ");
                                p = in.nextInt();
                            } else {
                                true_or_false3 = false;
                            }
                        }
                        myArray_of_divider[i] = p;
                        myArray_of_remainder[i] = b;
                    }

                }
                if (true_or_false4 == false) {
                    true_or_false2 = false;
                } else {
                    true_or_false2 = true;

                }
            }

            System.out.println("");
            for (int viv = 0; viv < k; viv++) {
                System.out.println("A" + "[" + (viv + 1) + "] " + " = " + myArray_of_remainder[viv] + " (mod " + myArray_of_divider[viv] + ")\n" );

            }

            boolean number_simple = true;
            for (int i_divider = 0; i_divider < k - 1; i_divider++) {
                for (int i2_divider = i_divider + 1; i2_divider < k; i2_divider++) {
                    long number1 = Math.abs(myArray_of_divider[i_divider]);
                    long number2 = Math.abs(myArray_of_divider[i2_divider]);
                    long res;
                    if (number1 < number2) {
                        long number = number1;
                        number1 = number2;
                        number2 = number;
                    }
                    do {
                        res = number1 % number2;
                        number1 = number2;
                        number2 = res;
                    } while (res != 0);
                    if (number1 != 1) {
                        System.out.print("nsk " + number1 + " for ");
                        System.out.println(" mod " + myArray_of_divider[i_divider] +
                                " and mod " + myArray_of_divider[i2_divider] +
                                ", so they are not mutually simple");
                        number_simple = false;
                    }
                }
            }
            if (number_simple == false) {
                System.exit(0);
            }

            start = System.nanoTime();
            long d_n = myArray_of_divider[0];
            long n2_while = myArray_of_remainder[0];
            int i_while = 1;
            for (int i_n = 0; i_n < k - 1; i_n++) {
                i_while = 1;
                long P_i_1 = d_n % myArray_of_divider[i_n + 1];
                long B2 = n2_while + (i_while - 1) * P_i_1;
                while ((n2_while + (i_while - 1) * P_i_1) % myArray_of_divider[i_n + 1] !=
                        myArray_of_remainder[i_n + 1]
                        && i_while < myArray_of_divider[i_n + 1] + 1) {
                    i_while++;

                }
                i_while++;
                n2_while = n2_while + (i_while - 2) * d_n;
                System.out.println("Step number " + (i_n + 2));
                System.out.println("N_n = " + n2_while);
                d_n = d_n * myArray_of_divider[i_n + 1];
                System.out.println("\n");

            }
        }
        else {
            System.out.println("U enter wrong number of pair of  numbers");
        }

        //Date md2 = new Date();
        //long start_md2 = md2.getTime();
        long end = System.nanoTime();
        long elapsedTime = end - start;

        System.out.printf("time in nanoseconds equal to %.5f %n", (double) (elapsedTime));
    }
}





