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

console.log(exports.palindrome('able was i ere i saw elba'));

exports.bottles = function() {

};

exports.romanNum = function() {

};
