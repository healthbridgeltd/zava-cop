function Person() {
  this.age = 0;

  let interval = setInterval(() => {
    this.age++;
    console.log(this.age); // What will this print out?
  }, 100);

  setTimeout(() => {
    clearInterval(interval);
    interval = null;
  }, 3000);
}

const p = new Person();