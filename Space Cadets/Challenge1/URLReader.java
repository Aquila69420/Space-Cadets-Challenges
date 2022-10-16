package Challenge1;
import java.net.*;
import java.io.*;
import java.util.Scanner;



public class URLReader {
    public static void main(String[] args) throws Exception {

        Scanner scanner = new Scanner(System.in); // Create a Scanner object
        System.out.println("Enter the email address:"); // Prompt user to enter email address
        String email = scanner.nextLine(); // Read user input
        scanner.close(); // Close the scanner

        String url = "https://www.ecs.soton.ac.uk/people/" + email; // Create the URL
        System.out.println("Your url is :" + url); // Print the URL

        URL link = new URL(url); // Create a URL object
        BufferedReader br = new BufferedReader(new InputStreamReader(link.openStream())); // Create a BufferedReader object
        String line; // Create a string to hold the line
        while ((line = br.readLine()) != null) { // While there is a line
            if (line.contains("og:title")) { // If the line contains the og:title (property containing the name)
                String name = line.substring(35); // Create a string to hold the name
                name = name.replace("\"", ""); // Remove the quotation marks
                String Name = name.replaceAll("/>", ""); // Remove the closing tag
                System.out.println(Name); // Print the name
                break; // Break the loop
            }
        }

        br.close(); // Close the BufferedReader
    }
}