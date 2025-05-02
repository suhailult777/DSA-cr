let capacity = 10;
let size = 0; // Initialize size to 0
let dynamicArray = [];

const add = (data) => {

    if (size >= capacity) {
        grow();
    }
    dynamicArray[size] = data;
    size++;

}

const insert = (index, data) => {

    if (size >= capacity) { // Fixed typo 'sixe' and operator
        grow();
    }

    for (let i = size; i > index; i--) {
        dynamicArray[i] = dynamicArray[i - 1];
    }

    dynamicArray[index] = data;
    size++;

}

const remove = (data) => {

    for (let i = 0; i < size; i++) {
        if (dynamicArray[i] == data) {
            for (let j = 0; j < (size - i - 1); j++) {
                dynamicArray[i + j] = dynamicArray[i + j + 1];
            }
            size--;
            if (size <= capacity / 3) {
                shrink();
            }
            break;
        }
    }
}

const search = (data) => {
    for (let i = 0; i < size; i++) {
        if (dynamicArray[i] == data) {
            return i;
        }
    }
    return -1;
}

let grow = () => {

    let newCapacity = capacity * 2;
    let newArray = new Array(newCapacity);

    for (let i = 0; i < size; i++) { // Only copy up to size
        newArray[i] = dynamicArray[i];
    }

    dynamicArray = newArray;
    capacity = newCapacity;

}

let shrink = () => {

    let newCapacity = Math.floor(capacity / 3); // Ensure integer result
    let newArray = new Array(newCapacity);

    for (let i = 0; i < size; i++) { // Only copy up to size
        newArray[i] = dynamicArray[i];
    }

    dynamicArray = newArray;
    capacity = newCapacity;

}

// --- Example Usage ---
console.log("Initial state:", { dynamicArray, size, capacity });

add(10);
add(20);
add(30);
console.log("After adding 3 elements:", { dynamicArray: dynamicArray.slice(0, size), size, capacity });

insert(1, 15);
console.log("After inserting 15 at index 1:", { dynamicArray: dynamicArray.slice(0, size), size, capacity });

remove(20);
console.log("After removing 20:", { dynamicArray: dynamicArray.slice(0, size), size, capacity });

console.log("Search for 15:", search(15));
console.log("Search for 99:", search(99));

// Trigger grow
console.log("\nTriggering grow...");
for (let i = 0; i < 8; i++) {
    add(100 + i);
}
console.log("After adding 8 more elements (grow triggered):", { dynamicArray: dynamicArray.slice(0, size), size, capacity });

// Trigger shrink
console.log("\nTriggering shrink...");
for (let i = 0; i < 8; i++) {
    remove(100 + i);
}
console.log("After removing 8 elements (shrink triggered):", { dynamicArray: dynamicArray.slice(0, size), size, capacity });
