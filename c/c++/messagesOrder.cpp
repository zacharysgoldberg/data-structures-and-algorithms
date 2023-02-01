#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

class Message {
private:
    std::string text;
    static int id;  // keeping track of all ids for duration of program
    int curr_id;

public:
    Message() { curr_id = id++; }

    Message(std::string txt): text{ txt }, curr_id(id++) {}

    const string& get_text() {
        return text;
    }

    bool operator < (const Message& message) {
        if (curr_id < message.curr_id) return true;
        else return false;
    }
};

// Instantiate id outside of class scope
int Message::id = 0;

class MessageFactory {
public:
    MessageFactory() {}
    Message create_message(const string& text) {
        Message message = Message(text);
        return message;
    }
};

class Recipient {
public:
    Recipient() {}
    void receive(const Message& msg) {
        messages_.push_back(msg);
    }
    void print_messages() {
        fix_order();
        for (auto& msg : messages_) {
            cout << msg.get_text() << endl;
        }
        messages_.clear();
    }
private:
    void fix_order() {
        sort(messages_.begin(), messages_.end());
    }
    vector<Message> messages_;
};

class Network {
public:
    static void send_messages(vector<Message> messages, Recipient& recipient) {
        // simulates the unpredictable network, where sent messages might arrive in unspecified order
        random_shuffle(messages.begin(), messages.end());
        for (auto msg : messages) {
            recipient.receive(msg);
        }
    }
};



int main() {
    MessageFactory message_factory;
    Recipient recipient;
    vector<Message> messages;
    string text;
    while (getline(cin, text)) {
        messages.push_back(message_factory.create_message(text));
    }
    Network::send_messages(messages, recipient);
    recipient.print_messages();
}
