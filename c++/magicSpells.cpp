#include <iostream>
#include <vector>
#include <string>

class Spell {
private:
    std::string scrollName;
public:
    Spell(): scrollName("") { }
    Spell(std::string name): scrollName(name) { }
    virtual ~Spell() { }
    std::string revealScrollName() {
        return scrollName;
    }
};

class Fireball: public Spell {
private: int power;
public:
    Fireball(int power): power(power) { }
    void revealFirepower() {
        std::cout << "Fireball: " << power << std::endl;
    }
};

class Frostbite: public Spell {
private: int power;
public:
    Frostbite(int power): power(power) { }
    void revealFrostpower() {
        std::cout << "Frostbite: " << power << std::endl;
    }
};

class Thunderstorm: public Spell {
private: int power;
public:
    Thunderstorm(int power): power(power) { }
    void revealThunderpower() {
        std::cout << "Thunderstorm: " << power << std::endl;
    }
};

class Waterbolt: public Spell {
private: int power;
public:
    Waterbolt(int power): power(power) { }
    void revealWaterpower() {
        std::cout << "Waterbolt: " << power << std::endl;
    }
};

class SpellJournal {
public:
    static std::string journal;
    static std::string read() {
        return journal;
    }
};
std::string SpellJournal::journal = "";

void counterspell(Spell* spell) {
    // 
    if (Fireball* fireball = dynamic_cast<Fireball*>(spell)) {
        fireball->revealFirepower();
    }
    else if (Frostbite* frostbite = dynamic_cast<Frostbite*>(spell)) {
        frostbite->revealFrostpower();
    }
    else if (Thunderstorm* thunderstorm = dynamic_cast<Thunderstorm*>(spell)) {
        thunderstorm->revealThunderpower();
    }
    else if (Waterbolt* waterbolt = dynamic_cast<Waterbolt*>(spell)) {
        waterbolt->revealWaterpower();
    }
    else {
        std::string spellName = spell->revealScrollName();
        std::string spellJournal = SpellJournal::read();

        // LCS
        int m = spellName.length(), n = spellJournal.length();
        int spellMatrix[m + 1][n + 1];

        for (int i = 0; i <= m; i++) {
            for (int j = 0; j <= n; j++) {
                if (i == 0 || j == 0)
                    spellMatrix[i][j] = 0;

                else if (spellName[i - 1] == spellJournal[j - 1])
                    spellMatrix[i][j] = spellMatrix[i - 1][j - 1] + 1;

                else
                    spellMatrix[i][j] = std::max(spellMatrix[i - 1][j],
                        spellMatrix[i][j - 1]);
            }
        }
        std::cout << spellMatrix[m][n] << '\n';
    }
}

class Wizard {
public:
    Spell* cast() {
        Spell* spell;
        std::string s; std::cin >> s;
        int power; std::cin >> power;
        if (s == "fire") {
            spell = new Fireball(power);
        }
        else if (s == "frost") {
            spell = new Frostbite(power);
        }
        else if (s == "water") {
            spell = new Waterbolt(power);
        }
        else if (s == "thunder") {
            spell = new Thunderstorm(power);
        }
        else {
            spell = new Spell(s);
            std::cin >> SpellJournal::journal;
        }
        return spell;
    }
};

int main() {
    int T;
    std::cin >> T;
    Wizard Arawn;
    while (T--) {
        Spell* spell = Arawn.cast();
        counterspell(spell);
    }
}