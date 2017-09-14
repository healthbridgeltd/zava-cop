let fruits = new Map();

const myFunc = () => {
  return true;
};

fruits.set(1, 'Apple');
fruits.set(2, 'banana');
fruits.set(3, 'Grape');
fruits.set(myFunc, 'key is a function');

console.log(fruits.size); // What will this print out?
console.log(fruits.get(2)); // What will this print out?

fruits.forEach((value, key) => {
  console.log(`Fruit ${value} is ${key}`); // What will this print out?
});

const arrayFruit = [
  [1, 'Apple'],
  [2, 'banana'],
  [3, 'Grape'],
];

let fruitMap = new Map(arrayFruit);

console.log(fruitMap.get(1)); // What will this print out?

for(let [key, fr] of fruitMap) {
  console.log(`Friut ${key} is ${fr}`); // What will this print out?
}