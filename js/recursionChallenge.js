exports.factorial = function(num) {
    if (num === 1){
        return num;
    } else {
        return num * exports.factorial(num - 1);
    }
    
};

// console.log(exports.factorial(7));

exports.palindrome = function(string) {
    if (string.length <= 1){
        return(true)
    }
    if (string[0] !== string[string.length - 1]){  // first and last letters don't match
		return(false)
    }
    return exports.palindrome(string.slice(1,-1));
};

//console.log(exports.palindrome('able was i ere i saw elba'));

exports.bottles = function(num) {
    if ( num === 1){
        return(console.log("Take one down and pass it around, 1 bottle of beer on the wall. \n1 bottle of beer on the \
wall, 1 bottle of beer.\nTake one down and pass it around, no more bottles of beer on the  \
wall. \nNo more bottles of beer on the wall, no more bottles of beer. \nGo to the store and buy \
some more, 99 bottles of beer on the wall."));
    }
    console.log(`${num} Bottles of beer on the wall, ${num} bottles of beer.\nTake one \
down pass it around, ${num - 1} more on the wall.`);

    exports.bottles(num - 1);
};

//console.log(exports.bottles(99));

exports.romanNum = function(num) {
    let BASE_CASES = {"": 0, "M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1};
    if (num in BASE_CASES){
        return BASE_CASES[num];
    }
    let first, second = map(roman_num, num.slice(0, 2)); // js equivalent???
    if (first < second){
        return(second - first + romanNum(num.slice(2)))
    } else {
        return(first + romanNum(num.slice(1)));
    };
};

console.log(exports.romanNum('XX'));