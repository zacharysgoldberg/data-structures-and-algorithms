#include<bits/stdc++.h>
#include <vector>

struct Workshop {
    int startTime_, duration_, endTime_;
};

struct Available_Workshops {
    int n_;
    std::vector<Workshop> workshops = std::vector<Workshop>(n_);

    Available_Workshops(int n): n_{ n } {}
};

// For sorting end times 
bool compare(Workshop& workshop1, Workshop& workshop2) {
    return workshop1.endTime_ < workshop2.endTime_;
}

Available_Workshops* initialize(int start_time[], int duration[], int n) {
    Available_Workshops* availableWorkshops = new Available_Workshops(n);

    for (int i = 0; i < n; i++) {
        availableWorkshops->workshops[i].startTime_ = start_time[i];
        availableWorkshops->workshops[i].duration_ = duration[i];
        availableWorkshops->workshops[i].endTime_ = start_time[i] + duration[i];
    }
    sort(availableWorkshops->workshops.begin(), availableWorkshops->workshops.end(), compare);
    return availableWorkshops;
}

int CalculateMaxWorkshops(Available_Workshops* ptr) {
    int count = 0;
    int curEndTime = 0;

    for (int i = 0; i < ptr->n_; i++) {
        if (ptr->workshops[i].startTime_ >= curEndTime) {
            curEndTime = ptr->workshops[i].endTime_;
            count += 1;
        }
    }
    return count;
}

int main(int argc, char* argv[]) {
    int n; // number of workshops
    std::cin >> n;
    // create arrays of unknown size n
    int* start_time = new int[n];
    int* duration = new int[n];

    for (int i = 0; i < n; i++) {
        std::cin >> start_time[i];
    }
    for (int i = 0; i < n; i++) {
        std::cin >> duration[i];
    }

    Available_Workshops* ptr;
    ptr = initialize(start_time, duration, n);
    std::cout << CalculateMaxWorkshops(ptr) << '\n';
}
