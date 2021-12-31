#include <iostream>
#include <string>
#include "Animal.h"
#include "childAnimal.h"

using namespace std ;

int main() {
    // Mammal m("Flippy", Blue);
    // m.speak();
    // Dog d("Goofy", Brown, "Gerald");
    // d.speak();
    // d.move();

    // Animal *animalPtr = new Dog("Lassie", White, "Andy");
    // animalPtr->speak();
    // animalPtr->move();
    // delete animalPtr;

    // Dog dogi("Lassie", White, "Andy");
    // Mammal *aniPtr = &dogi;
    // Mammal &aniRef = dogi;
    // Mammal aniVal = dogi;
    // aniPtr->speak();
    // aniRef.speak();
    // aniVal.speak();

    // 4. Build a Zoo
    int choice = 0;
    Mammal **mammal = new Mammal*[3];
    mammal[0] = new Dog("Lassie", White, "Andy");
    mammal[1] = new Cat("Jolly", Black, "Aaron");
    mammal[2] = new Lion("George", Brown, "Zen");
    
    while (choice < 5) {
        cout << "\nSelect the animal to send to Zoo :\n(1) Dog (2) Cat (3) Lion (4) Move all animals (5) Quit" << endl;
        cin >> choice;
        
        switch(choice) {
            case 1: case 2: case 3:
                cout << mammal[choice-1]->getName() << " is being sent to the Zoo." << endl;
                mammal[choice-1]->move();
                mammal[choice-1]->speak();
                mammal[choice-1]->eat();
                break;
            case 4:
                for (int i = 0; i < 3; i++) {
                    cout << endl;
                    mammal[i]->move();
                    mammal[i]->speak();
                    mammal[i]->eat();
                }
                break;
        }
    }

    for (int i = 0; i < 3; i++)
        delete mammal[i];
    delete [] mammal;
    
    cout << "Program exiting... "<< endl ; 
    return 0;
}
