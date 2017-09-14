class Car {
  constructor() {
    this.wheels = 4;
  }

  print() {
    console.log(`Wheels: ${this.wheels}`);
  }
}

// http://images.autotrader.com/scaler/780/520/cms/images/oversteer/2017/03-mar/isetta/263359.jpg
class BMWIsetta extends Car {
  constructor() {
    super();

    this.wheels = 3;
  }
}

let bmw = new BMWIsetta();
bmw.print();