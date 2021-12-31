#include <iostream>
#include <string>
#include "childAnimal.h"

using namespace std ;


Dog::Dog() : Mammal(), _owner("unknown") {
    cout << "constructing Dog object " << Dog::getName() << endl;
}

Dog::Dog(string n, COLOR c, string o) : Mammal(n, c), _owner(o) {
    cout << "constructing Dog object " << Dog::getName() << endl;
}

Dog::~Dog() {
    cout << "destructing Dog object " << Dog::getName() << endl;
}

void Dog::speak() const {
    cout << "Woof" << endl;
}

void Dog::move() const {
    cout << "Dog move " << endl;
}

void Dog::eat() const {
    cout << "Dog eat " << endl;
}


Cat::Cat() : Mammal(), _owner("unknown") {
    cout << "constructing Cat object " << Cat::getName() << endl;
}

Cat::Cat(string n, COLOR c, sKtring o) : Mammal(n, c), _owner(o) {
    cout << "constructing Cat object " << Cat::getName() << endl;
}

Cat::~Cat() {
    cout << "destructing Cat object " << Cat::getName() << endl;
}

void Cat::speak() const {
    cout << "Meow" << endl;
}

void Cat::move() const {
    cout << "Cat move " << endl;
}

void Cat::eat() const {
    cout << "Cat eat " << endl;
}


Lion::Lion() : Mammal(), _owner("unknown") {
    cout << "constructing Lion object " << Lion::getName() << endl;
}

Lion::Lion(string n, COLOR c, string o) : Mammal(n, c), _owner(o) {
    cout << "constructing Lion object " << Lion::getName() << endl;
}

Lion::~Lion() {
    cout << "destructing Lion object " << Lion::getName() << endl;
}

void Lion::speak() const {
    cout << "Roar" << endl;
}

void Lion::move() const {
    cout << "Lion move " << endl;
}

void Lion::eat() const {
    cout << "Lion eat " << endl;
}
