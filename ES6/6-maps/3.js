let fruitsMap = new Map();

fruitsMap.set('1', 'Apple');
fruitsMap.set('3', 'Grape');
fruitsMap.set('2', 'banana');

const vegObj = {
  1: 'Onion',
  3: 'Garlic',
  2: 'Lettuce',
};

let vegMap = new Map();

fruitsMap.set(vegMap, vegObj);

console.log(fruitsMap.get(vegMap));