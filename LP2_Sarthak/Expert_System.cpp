#include <iostream>
#include <string>
using namespace std;

void handleRequest(int type) {
    if (type == 1) {
        string source, destination;
        int tickets;
        cout << "Enter source city: ";
        getline(cin, source);
        cout << "Enter destination city: ";
        getline(cin, destination);
        cout << "How many tickets? ";
        cin >> tickets;
        cin.ignore();
        cout << "Booked " << tickets << " ticket(s) from " << source << " to " << destination << ".\n";
    } else if (type == 2) {
        cout << "Track flight: https://www.example.com/track-flight-status\n";
    } else if (type == 3) {
        int claim;
        cout << "Enter baggage claim number: ";
        cin >> claim;
        cin.ignore();
        cout << "Go to counter " << (claim % 2 == 0 ? "2" : "3") << " for pickup.\n";
    } else if (type == 4) {
        string feedback;
        cout << "Enter your feedback: ";
        getline(cin, feedback);
        cout << "Thank you for your feedback!\n";
    } else if (type == 5) {
        string flight;
        cout << "Enter flight number: ";
        getline(cin, flight);
        cout << "Flight " << flight << " is at 3 PM today.\n";
    } else if (type == 6) {
        string id;
        cout << "Enter cargo ID: ";
        getline(cin, id);
        cout << "Cargo " << id << " pickup at 5 PM today.\n";
    } else {
        cout << "Invalid choice.\n";
    }
}

int main() {
    while (true) {
        cout << "\n--- Airline Helpdesk ---\n";
        string name;
        cout << "Enter your name: ";
        getline(cin, name);

        cout << "\nChoose a service:\n";
        cout << "1. Flight Booking\n";
        cout << "2. Flight Status\n";
        cout << "3. Baggage Inquiry\n";
        cout << "4. Feedback\n";
        cout << "5. Airline Schedule\n";
        cout << "6. Cargo Schedule\n";
        cout << "Choice: ";
        int choice;
        cin >> choice;
        cin.ignore();

        handleRequest(choice);

        char again;
        cout << "\nContinue? (y/n): ";
        cin >> again;
        cin.ignore();
        if (again == 'n' || again == 'N') {
            cout << "Goodbye!\n";
            break;
        }
    }
    return 0;
}