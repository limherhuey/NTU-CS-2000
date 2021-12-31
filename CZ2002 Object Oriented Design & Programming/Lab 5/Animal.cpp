#include <iostream>
#include <string>
#include "Animal.h"

using namespace std ;


Animal::Animal() : _name("unknown") {
    cout << "constructing Animal object "<< _name << endl ; 
}

Animal::Animal(string n, COLOR c) : _name(n), _color(c) {
    cout << "Constructing Animal object " << _name << " with color " << nameCOLOR[_color] << endl;
}

Animal::~Animal() {
    cout << "destructing Animal object "<< _name << endl ; 
}

string Animal::getName() const {
    return _name;
}

void Animal::speak() const {
    cout << "Animal speaks "<< endl ; 
}


Mammal::Mammal() : Animal() {
    cout << "constructing Mammal object " << Mammal::getName() << endl;
}

Mammal::Mammal(string n, COLOR c) : Animal(n, c) {
    cout << "constructing Mammal object " << Mammal::getName() << endl;
}

Mammal::~Mammal() {
    cout << "destructing Mammal object " << Mammal::getName() << endl;
}

void Mammal::eat() const {
    cout << "Mammal eat " << endl;
}

void Mammal::move() const {
    cout << "Mammal move " << endl;
}
