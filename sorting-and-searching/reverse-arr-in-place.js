'use strict'
//reverse an array of integers in place
let arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr.map((n) => console.log(n))

let reverse = arr => {
    let temp = ''
    for(let i = 0; i < arr.length / 2; i++) {
        let opp =  arr.length - i - 1   
        temp = arr[opp]
        arr[opp] = arr[i]
        arr[i] = temp 
    }
}


reverse(arr)
arr.map((n) => console.log(n))
