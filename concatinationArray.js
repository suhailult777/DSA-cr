

const getconcatinationArray = (nums) => {

    let n = nums.length;
    let ans = new Array(2 * n);

    for (let i = 0; i < nums.length; i++) {
        ans[i] = nums[i];
        ans[i + n] = nums[i];
    }

    return ans;
}

console.log(getconcatinationArray([1, 2, 1])); // Output: [1, 2, 1, 1, 2, 1]
console.log(getconcatinationArray([1, 3, 2, 1])); // Output: [1, 3, 2, 1, 1, 3, 2, 1]
