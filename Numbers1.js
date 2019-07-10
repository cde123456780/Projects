let findDecimalPlaces = function() {
  //This function asks for the user for the number of decimal places
  let decimals = "";
  while (decimals == "") {
    let userInput = prompt("Enter the number of decimal places: ");
    if (typeof(userInput) == "number" && userInput > 0) {
      if (userInput < 49) {
        decimals = userInput;
      } else {
        console.log("Input must be less than 49");
      }

    } else if (typeof(userInput) != "number") {
      console.log("Input must be a number");
    } else {
      console.log("Input must be greater than 0");
    }
  }
  return decimals;
}

let printPi = function(decimals) {
  //This function prints out Pi to the given number of decimal places
  console.log(Math.PI.toFixed(decimals));
}

let decimals = findDecimalPlaces()
printPi(decimals);
