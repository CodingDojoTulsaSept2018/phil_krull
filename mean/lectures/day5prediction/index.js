// ----------------------------------------- Question I -----------------------------------------
function crazy(a, b, c, d) {
    if (a > 0) {
        return b(d(a));
    }
    else {
        return c(b(a));
    }
}
var output = crazy(5, function (a) {
    for (var i = 1; i < a; i++) {
        return a * i;
    }
}, function (a) {
    return a - 6;
}, function (a) {
    return a + 7;
});
console.log("output", output);

function caller(a, b, c) {
    console.log(a);
    console.log(c(b(a)));
    return b(a);
}
var result = caller(5, function (num) {
    var sum = num;
    for (var i = 0; i < num; i++) {
        sum -= i;
    }
    return sum;
}, function (num) {
    if (num > 0) {
        return num;
    }
    else {
        return 0;
    }
})
console.log('result', result);

// ----------------------------------------- Question II -----------------------------------------
function foo(a,b,c){
    if(a > 5){
        return c(b(a));
    }
    else {
        return b(c(a));
    }
}
var bar = foo(-2, function(a){
    var sum = 1;
    for(var i=a; i>0; i--){
        sum += i;
    }
    return sum;
}, function(a){
    return a + 5;
})
console.log(bar);
