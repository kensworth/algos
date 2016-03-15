// flatten an object
(function() {
    'use strict'
    let obj =  {
		key1: 'k1',
		key2: 'k2',
		key3: {
			k3a: 'nested-k3a',
			k3b: 'nested-k3b'
		},
		key4: {
			k4a: {
				k4a1: 'doublenested-k4a'
			},
			k4b: 'nested-k4b'
		},
		key5: 'k5'
	},
    flat = {}  

    function flatten(obj) {
        for(let key in obj) {
            if(typeof obj[key] === 'object') {
                flatten(obj[key]) 
            } 
            else {
                flat[key] = obj[key] 
            }
        }
    } 
    flatten(obj)
    let flatJSON = JSON.stringify(flat, null, 4)
    console.log(flatJSON)
}())
