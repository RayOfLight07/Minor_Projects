#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX 100

typedef struct {
    int train_number;
    char train_name[50];
    char from[50];
    char to[50];
    int available_seats;
} Train;

typedef struct {
    char name[50];
    int train_number;
    int seat_number;
} Ticket;

Train trains[MAX];
Ticket tickets[MAX];
int train_count = 0;
int ticket_count = 0;

void add_train() {
    printf("Enter Train Number: ");
    scanf("%d", &trains[train_count].train_number);

    printf("Enter Train Name: ");
    scanf("%s", trains[train_count].train_name);

    printf("From: ");
    scanf("%s", trains[train_count].from);

    printf("To: ");
    scanf("%s", trains[train_count].to);

    printf("Available Seats: ");
    scanf("%d", &trains[train_count].available_seats);

    train_count++;
    printf("Train added successfully!\n");
}

void display_trains() {
    printf("\nAvailable Trains:\n");
    printf("Train No.\tTrain Name\tFrom\tTo\tSeats Available\n");
    for (int i = 0; i < train_count; i++) {
        printf("%d\t\t%s\t\t%s\t%s\t%d\n", trains[i].train_number, trains[i].train_name, trains[i].from, trains[i].to, trains[i].available_seats);
    }
}

void book_ticket() {
    int train_no;
    printf("Enter Train Number: ");
    scanf("%d", &train_no);

    int train_index = -1;
    for (int i = 0; i < train_count; i++) {
        if (trains[i].train_number == train_no) {
            train_index = i;
            break;
        }
    }

    if (train_index == -1) {
        printf("Train not found!\n");
        return;
    }

    if (trains[train_index].available_seats == 0) {
        printf("No seats available!\n");
        return;
    }

    printf("Enter your name: ");
    scanf("%s", tickets[ticket_count].name);

    tickets[ticket_count].train_number = train_no;
    tickets[ticket_count].seat_number = trains[train_index].available_seats;

    trains[train_index].available_seats--;

    printf("Ticket booked successfully! Seat Number: %d\n", tickets[ticket_count].seat_number);
    ticket_count++;
}

void display_booked_tickets() {
    printf("\nBooked Tickets:\n");
    printf("Name\t\tTrain No.\tSeat No.\n");
    for (int i = 0; i < ticket_count; i++) {
        printf("%s\t\t%d\t\t%d\n", tickets[i].name, tickets[i].train_number, tickets[i].seat_number);
    }
}

int main() {
    int choice;

    while (1) {
        printf("\nRailway Management System\n");
        printf("1. Add Train\n");
        printf("2. Display Available Trains\n");
        printf("3. Book Ticket\n");
        printf("4. Display Booked Tickets\n");
        printf("5. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                add_train();
                break;
            case 2:
                display_trains();
                break;
            case 3:
                book_ticket();
                break;
            case 4:
                display_booked_tickets();
                break;
            case 5:
                exit(0);
            default:
                printf("Invalid choice! Please try again.\n");
        }
    }

    return 0;
}
