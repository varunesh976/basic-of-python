import java.util.*;

public class CityList {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        ArrayList<String> cities = new ArrayList<>();

        System.out.print("Enter number of cities: ");
        int n = sc.nextInt();
        sc.nextLine();

        System.out.println("Enter city names:");
        for (int i = 0; i < n; i++) {
            cities.add(sc.nextLine());
        }

        // Append a city
        System.out.print("Enter city to append: ");
        String appendCity = sc.nextLine();
        cities.add(appendCity);

        // Insert a city
        System.out.print("Enter index: ");
        int index = sc.nextInt();
        sc.nextLine();

        System.out.print("Enter city to insert: ");
        String insertCity = sc.nextLine();
        cities.add(index, insertCity);

        // Search a city
        System.out.print("Enter city to search: ");
        String searchCity = sc.nextLine();

        if (cities.contains(searchCity)) {
            System.out.println("City found at index: " + cities.indexOf(searchCity));
        } else {
            System.out.println("City not found");
        }

        // Display cities starting with a letter
        System.out.print("Enter starting letter: ");
        char ch = sc.next().charAt(0);

        System.out.println("Cities starting with '" + ch + "':");

        for (String city : cities) {
            if (city.toLowerCase().startsWith(String.valueOf(ch).toLowerCase())) {
                System.out.println(city);
            }
        }

        sc.close();
    }
}
