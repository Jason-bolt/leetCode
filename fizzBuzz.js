function fizzBuzz(n) {
    valueArray = [];
    for (let i = 1; i <= n; i++) {
        value = '';
        if ((i % 3) === 0) {
            value += 'Fizz';
        }
        if ((i % 5) === 0) {
            value += 'Buzz';
        }
        if (value === '') {
            value = `${i}`;
        }
        valueArray.push(value);
        console.log(value);
    }
    console.log(valueArray);
}

function ascendingOrder(myArray) {
    const n = myArray.length;
    for (let i = 0; i < n - 1; i++) {
        for (let j = 0; j < n - i - 1; j++) {
            if (myArray[j] > myArray[j + 1]) {
                [myArray[j], myArray[j + 1]] = [myArray[j + 1], myArray[j]]
            }
        }
    }
    console.log(myArray);
}

function descendingOrder(myArray) {
    const n = myArray.length;
    for (let i = 0; i < n - 1; i++) {
        for (let j = 0; j < n - i - 1; j++) {
            if (myArray[j] < myArray[j + 1]) {
                [myArray[j], myArray[j + 1]] = [myArray[j + 1], myArray[j]]
            }
        }
    }
    console.log(myArray);
}

// fizzBuzz(5);
// ascendingOrder([3, 4, 6, 3]);
// descendingOrder([3, 4, 6, 3]);
