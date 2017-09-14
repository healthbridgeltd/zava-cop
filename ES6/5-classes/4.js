class Parent {
  static whoami() {
    return 'Parent';
  }

  lognameA() {
    console.log(Parent.whoami());
  }

  lognameB() {
    console.log(this.constructor.whoami());
  }
}

class Child extends Parent {
  static whoami() {
    return 'Child';
  }
}

const child = new Child();

child.lognameA(); // What will this print out?
child.lognameB(); // And this other one?