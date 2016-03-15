'use strict'
//reverse an array of integers in place
let arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

let reverse = arr => {
    for(let i = 0; i < arr.length / 2; i++) {
        let opp =  arr.length - i - 1   
        arr[i] += arr[opp]
        arr[opp] = arr[i] - arr[opp]
        arr[i] -= arr[opp]
    }
}


reverse(arr)
arr.map((n) => console.log(n))
