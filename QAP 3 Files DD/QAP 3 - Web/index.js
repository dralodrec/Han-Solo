// Desc: This program prints Mo’s Lawncare Services - Customer Invoice using javascript
// Author: Darrell Declaro
// Dates: 11/11/2025


var $ = function (id) {
  return document.getElementById(id);
};


// Define format options for printing.
const cur2Format = new Intl.NumberFormat("en-CA", {
  style: "currency",
  currency: "CAD",
  minimumFractionDigits: "2",
  maximumFractionDigits: "2",
});

const per0Format = new Intl.NumberFormat("en-CA", {
  style: "percent",
  minimumFractionDigits: "0",
  maximumFractionDigits: "0",
});

const com2Format = new Intl.NumberFormat("en-CA", {
  style: "decimal",
  minimumFractionDigits: "2",
  maximumFractionDigits: "2",
});

// function for capitalize first letter of each word. reference www.w3resource.com
function capital_letter(str) {
    str = str.split(" ");
    for (var i = 0, x = str.length; i < x; i++) {
        str[i] = str[i][0].toUpperCase() + str[i].substr(1);
    }
    return str.join(" ");
}
 


// Define program constants.
const BORDER_ = 0.28;
const MOWING_ = 0.04;
const FERTI_ = 0.03;

const HST_RATE = 0.15;
const ENVI_RATE = 0.014;


// Start main program here.

// Gather user input. add default value to the 
let inputName = prompt("Enter Customer Name: ", "john wakeham smith");
let inputStAdd = prompt("Enter Street Address: ", "36 bread and cheese road");
let inputCity = prompt("Enter City: ", "bay bulls");
let phone = prompt("Enter Phone Number: ", "XXX-XXX-XXXX");
let propertySize = parseFloat(prompt("Enter property size (sqft): ", 4561));

let CustName = capital_letter(inputName)
let StAdd = capital_letter(inputStAdd)
let City = capital_letter(inputCity)


// Generate program results.
let borderCost = 0.04 * propertySize * BORDER_
let mowingCost = 0.95 * propertySize * MOWING_
let fertilizerCost = propertySize * FERTI_

let totalCharges = borderCost + mowingCost + fertilizerCost

let HST = totalCharges * HST_RATE;
let enviTax = totalCharges * ENVI_RATE;

let invoiceTotal = totalCharges + HST + enviTax;


// Display results to the screen.
document.writeln("<br />");
document.writeln("<table class='resultstable'>");

document.writeln("<tr>");
document.writeln("<td colspan='2' class='centertext'>Mo's Lawncare Services - Customer Invoice</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td colspan='2'><br /><span>Customer Details:</span> <br /><br />");
document.writeln("<div class='indent'>" + CustName + "<br />" + 
                  StAdd + "<br />" + City + ", " + phone + "<br /><br /></div>")
document.writeln("<span>Property size (sqft): </span>" + propertySize)
document.writeln("<br /><br /></td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td>Border Cost:</td>");
document.writeln("<td class='righttext'>" + cur2Format.format(borderCost) + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td>Mowing Cost:</td>");
document.writeln("<td class='righttext'>" + cur2Format.format(mowingCost) + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td>Fertilizer Cost:</td>");
document.writeln("<td class='righttext'>" + cur2Format.format(fertilizerCost) + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td><br /></td>");
document.writeln("<td class='righttext'></td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td>Total Charges:</td>");
document.writeln("<td class='righttext'>" + cur2Format.format(totalCharges) + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td><br /></td>");
document.writeln("<td class='righttext'></td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td>Sales Tax (HST):</td>");
document.writeln("<td class='righttext'>" + cur2Format.format(HST) + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td>Environmental Tax:</td>");
document.writeln("<td class='righttext'>" + cur2Format.format(enviTax) + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td><br /></td>");
document.writeln("<td class='righttext'></td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td>Invoice Total:</td>");
document.writeln("<td class='righttext'>" + cur2Format.format(invoiceTotal) + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td colspan='2' class='centertext'>Turning Lawns into Landscapes</td>");
document.writeln("</tr>");

document.writeln("</table><br />")
