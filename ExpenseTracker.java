import java.util.ArrayList;
import java.util.Scanner;

// Class to represent an Expense
class Expense {
    String category;
    double amount;

    public Expense(String category, double amount) {
        this.category = category;
        this.amount = amount;
    }

    @Override
    public String toString() {
        return "Category: " + category + ", Amount: $" + amount;
    }
}

// Expense Tracker class
public class ExpenseTracker {
    private double totalIncome = 0;
    private double totalExpenses = 0;
    private ArrayList<Expense> expensesList = new ArrayList<>();

    // Method to add income
    public void addIncome(double income) {
        totalIncome += income;
        System.out.println("Income of $" + income + " added.");
    }

    // Method to add expense
    public void addExpense(String category, double amount) {
        expensesList.add(new Expense(category, amount));
        totalExpenses += amount;
        System.out.println("Expense of $" + amount + " added in category: " + category);
    }

    // Method to view summary
    public void viewSummary() {
        System.out.println("\n--- Financial Summary ---");
        System.out.println("Total Income: $" + totalIncome);
        System.out.println("Total Expenses: $" + totalExpenses);
        System.out.println("Current Balance: $" + (totalIncome - totalExpenses));
    }

    // Method to list all expenses
    public void listExpenses() {
        System.out.println("\n--- List of Expenses ---");
        for (Expense expense : expensesList) {
            System.out.println(expense);
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ExpenseTracker tracker = new ExpenseTracker();
        int choice;

        // Menu-driven interface
        do {
            System.out.println("\n--- Expense Tracker Menu ---");
            System.out.println("1. Add Income");
            System.out.println("2. Add Expense");
            System.out.println("3. View Summary");
            System.out.println("4. List Expenses");
            System.out.println("5. Exit");
            System.out.print("Enter your choice: ");
            choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    System.out.print("Enter income amount: ");
                    double income = scanner.nextDouble();
                    tracker.addIncome(income);
                    break;
                case 2:
                    System.out.print("Enter expense category: ");
                    String category = scanner.next();
                    System.out.print("Enter expense amount: ");
                    double amount = scanner.nextDouble();
                    tracker.addExpense(category, amount);
                    break;
                case 3:
                    tracker.viewSummary();
                    break;
                case 4:
                    tracker.listExpenses();
                    break;
                case 5:
                    System.out.println("Exiting... Goodbye!");
                    break;
                default:
                    System.out.println("Invalid choice! Please choose again.");
            }
        } while (choice != 5);

        scanner.close();
    }
}
