process.stdin.resume();
process.stdin.setEncoding('ascii');

var input_stdin = "";
var input_stdin_array = "";
var input_currentline = 0;

process.stdin.on('data', function (data) {
    input_stdin += data;
});

process.stdin.on('end', function () {
    input_stdin_array = input_stdin.split("\n");
    main();
});

function readLine() {
    return input_stdin_array[input_currentline++];
}

/////////////// ignore above this line ////////////////////

function reverseShuffleMerge(s) {
    // Complete this function
}

function main() {
    var s = readLine();
    var result = reverseShuffleMerge(s);
    process.stdout.write("" + result + "\n");






// function switchOfStuff(val) {
//   var answer = "";
//   // Only change code below this line
//   switch(val) {
//     case 1:
//       if (val = 1) {
//         return "Your bigger than 4";
//       break;
//
//
//   }
//
//   // Only change code above this line
//   return answer;
// }

// Change this value to test
// switchOfStuff(1);

// Write a switch statement to set answer for the following ranges:
// 1-3 - "Low"
// 4-6 - "Mid"
// 7-9 - "High"


//
// function switchRange(value) {
//   answer = "";
//
//   switch(value) {
//     case 1:
//       return "Low";
//       break;
//     case 2:
//       return "Low";
//       break;
//     case 3:
//       return "Low";
//     }
// }
//
//
// console.log(switchRange(2));
//





















//
// function jerkOrNot(value) {
//   var verdict = "";
//
//   switch(value) {
//     case 1:
//       if(value == 1) {
//         return "your are a 1st degree jerk";
//       }
//     case 2:
//       if(value == 2) {
//         return "your a 2nd degree jerk";
//       }
//     case 3:
//       if(value == 3) {
//         return "your a 3rd degree jerk";
//       }
//     case 4:
//       if(value == 4) {
//         return "your a 4th degree jerk";
//       }
//     }
// }
//
// console.log(jerkOrNot(3));




// // Setup
// function abTest(a, b) {
//   // Only change code below this line
//   answer = "";
//   if (a < 0 || b < 0) {
//
//     return undefined;
//   }
//
//
//   // Only change code above this line
//
//   return Math.round(Math.pow(Math.sqrt(a) + Math.sqrt(b), 2));
// }
//
// // Change values below to test your code
// console.log(abTest(-2,2));
