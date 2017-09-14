class Rectangle {
  constructor(height, width) {
    this._height = height;
    this._width = width;
  }

  get area() {
    return this.calcArea();
  }

  set width(newWidth) {
    if (newWidth) {
      this._width = newWidth + 0.001;
    }
  }

  calcArea() {
    return this._height * this._width;
  }
}

const square = new Rectangle(10, 10);
console.log(square.area);

square.width = 11;
console.log(square._width);