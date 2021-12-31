#ifndef ANIMAL_H
#define ANIMAL_H

#include <iostream>
#include <string>

using namespace std ;

enum COLOR { Green, Blue, White, Black, Brown } ;

class Animal {
    public :
        Animal();
        Animal(string n, COLOR c);
        ~Animal();

        string getName() const;

        virtual void speak() const;
        virtual void move() const = 0;
        virtual void eat() const = 0;

    private :
        string _name;
        COLOR _color;
        const char *nameCOLOR[5] = {"Green", "Blue", "White", "Black", "Brown"};
};

class Mammal: public Animal {
    public:
        Mammal();
        Mammal(string n, COLOR c);
        ~Mammal();

        void eat() const;
        void move() const;
};

#endif