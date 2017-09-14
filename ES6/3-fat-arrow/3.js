function Person() {
  this.age = 0;

  let interval = setInterval(function () {
    this.age++;
    console.log(this.age); // What will this print out?
  }, 100);

  setTimeout(function () {
    clearInterval(interval);
    interval = null;
  }, 3000);
}

const p = new Person();