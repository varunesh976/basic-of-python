import java.util.Scanner;

public class EBBill {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String type;
        int units;
        double amount = 0;

        System.out.print("Enter Connection Type (domestic/commercial): ");
        type = sc.next().toLowerCase();

        System.out.print("Enter Units Consumed: ");
        units = sc.nextInt();

        if (type.equals("domestic")) {
            if (units <= 100)
                amount = 0;
            else if (units <= 200)
                amount = (units - 100) * 2;
            else if (units <= 500)
                amount = 100 * 2 + (units - 200) * 4;
            else
                amount = 100 * 2 + 300 * 4 + (units - 500) * 6;
        } else if (type.equals("commercial")) {
            if (units <= 100)
                amount = units * 2;
            else if (units <= 200)
                amount = 100 * 2 + (units - 100) * 4;
            else if (units <= 500)
                amount = 100 * 2 + 100 * 4 + (units - 200) * 6;
            else
                amount = 100 * 2 + 100 * 4 + 300 * 6 + (units - 500) * 7;
        } else {
            System.out.println("Invalid Connection Type");
            return;
        }

        System.out.println("Connection Type : " + type);
        System.out.println("Units Consumed  : " + units);
        System.out.println("Amount to be Paid : Rs. " + amount);
    }
}
