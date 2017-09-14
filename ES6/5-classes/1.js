class Car {

  constructor(doors = 4, seats = 5) {
    this.wheels = 4;
    this.steeringWheel = 1;

    // Initialisation the old school way:
    this.doors = doors;
    this.seats = seats;

    // A shorter method:
    Object.assign(this, { doors, seats });
  }

  print() {
    console.log(`
      The car has:
      - Wheels: ${this.wheels}
      - SteeringWheel: ${this.steeringWheel}
      - Doors: ${this.doors}
      - Seats: ${this.seats}
    `);
  }

}

const MercedesBenz = new Car(3, 4);
MercedesBenz.print();