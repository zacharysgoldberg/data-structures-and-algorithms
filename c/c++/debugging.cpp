#include <iostream>
#include <vector>

class HotelRoom {
private:
    int bedrooms_;
    int bathrooms_;

public:
    HotelRoom(int bedrooms, int bathrooms)
        : bedrooms_(bedrooms), bathrooms_(bathrooms) {}
    // added virtual (the most derived class uses their version of the function)
    virtual int get_price() {
        return 50 * bedrooms_ + 100 * bathrooms_;
    }
};

class HotelApartment: public HotelRoom {
public:
    HotelApartment(int bedrooms, int bathrooms)
        : HotelRoom(bedrooms, bathrooms) {}

    int get_price() {
        std::cout << HotelRoom::get_price() << '\n';
        return HotelRoom::get_price() + 100;
    }
};

int main() {
    int n;
    std::cin >> n;
    std::vector<HotelRoom*> rooms;
    for (int i = 0; i < n; ++i) {
        std::string room_type;
        int bedrooms;
        int bathrooms;
        std::cin >> room_type >> bedrooms >> bathrooms;
        if (room_type == "standard") {
            rooms.push_back(new HotelRoom(bedrooms, bathrooms));
        }
        else {
            rooms.push_back(new HotelApartment(bedrooms, bathrooms));
        }
    }

    int total_profit = 0;
    for (auto room : rooms) {
        total_profit += room->get_price();
    }
    std::cout << total_profit << '\n';

    for (auto room : rooms) {
        delete room;
    }
    rooms.clear();
}