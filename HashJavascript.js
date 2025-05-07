function HashTable() {
    let size = 10; // Fixed typo 'size' and operator
    let table = new Array(size);

    const _hash = (key) => {
        let hash = 0;
        for (let i = 0; i < key.length; i++) {
            hash = (hash * 31 + key.charCodeAt(i)) % size; // Improved hashing
        }
        return hash;
    }

    const put = (key, value) => {
        let index = _hash(key);
        if (!table[index]) {
            table[index] = [];
        }
        // Check if key exists and update value
        for (let entry of table[index]) {
            if (entry[0] === key) {
                entry[1] = value;
                return;
            }
        }
        table[index].push([key, value]);
    }

    const get = (key) => {
        let index = _hash(key);
        if (!table[index]) return undefined;
        for (let entry of table[index]) {
            if (entry[0] === key) {
                return entry[1];
            }
        }
        return undefined;
    }

    const display_hashes = () => {
        for (let i = 0; i < table.length; i++) {
            if (table[i]) {
                for (let entry of table[i]) {
                    console.log(`Key: ${entry[0]}, Hash: ${_hash(entry[0])}, Index: ${i}`);
                }
            }
        }
    }

    return {
        put,
        get,
        display_hashes
    }
}

// Test code remains the same...


let hashTable = HashTable();
hashTable.put("apple", 112);
hashTable.put("banana", 123);
hashTable.put("cherry", 124);
hashTable.put("pears", 145);
hashTable.put("watermelon", 156);
hashTable.put("grapes", 167);
hashTable.put("blackberry", 777);

console.log(hashTable.get("apple")); // 112
console.log(hashTable.get("banana")); // 123
console.log(hashTable.get("cherry")); // 124
console.log(hashTable.get("pears")); // 145
console.log(hashTable.get("watermelon")); // 156
console.log(hashTable.get("grapes")); // 167

hashTable.display_hashes(); // Display hash values


