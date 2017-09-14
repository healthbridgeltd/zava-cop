let fruitsMap = new Map();

const myFunc = () => true;

fruitsMap.set('1', 'Apple');
fruitsMap.set('3', 'Grape');
fruitsMap.set('2', 'banana');
fruitsMap.set(myFunc, 'key is a function');

// Maps are iterable.
fruitsMap.forEach((value, key) => {
  console.log(`Fruit ${value} is ${key}`);
});


const fruitsObj = {
  1: 'Apple',
  3: 'Grape',
  2: 'Banana',
};

for (let key in fruitsObj) {
  console.log(`Fruit ${fruitsObj[key]} is ${key}`);
}