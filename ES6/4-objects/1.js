const car = {}; // Shorthand for `new Object(null);`

Object.defineProperty(car, 'wheels', {
  value: 4,
  enumerable: true,
  writable: false,
  configurable: true,
});

Object.defineProperty(car, 'steeringWheel', {
  value: true,
  enumerable: false,
  writable: false,
  configurable: false,
});

let doors = 3;
Object.defineProperty(car, 'doors', {
  get: () => doors,
  set: (newDoors) => {
    doors = newDoors + 1;
  },
  enumerable: true,
  configurable: true,
});

car.doors = 4; // What will the new value of doors after this?

Object.defineProperty(car, 'gears', {
  value: 6,
  enumerable: true,
  writable: false,
  configurable: true,
});

// Object.defineProperty(car, 'gears', { enumerable: false });

car.gears = 5; // What does this actually do?

Object.defineProperty(car, 'colour', {
  value: 'green',
  enumarable: true,
  writable: false,
  configurable: false,
});

for (let i in car) {
  console.log(i, car[i]);
}

// Object.freeze
// Object.assign
