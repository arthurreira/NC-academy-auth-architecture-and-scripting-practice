const fs = require('fs');

// Function to read a file and print its content
function readFileAndPrint(fileName) {
    fs.readFile(fileName, 'utf8', function(err, data) {
        if (err) {
            console.log("Error reading file: " + err);
            return;
        }
        console.log("File content: " + data)
    });
}

// Function to write data to a file
function writeFile(fileName, data) {
    fs.writeFile(fileName, data, function(err) {
        if (err) {
            console.log("Error writing file: " + err);
            return;
        }
        console.log("Data written successfully");
    })
}

// Using the functions
let file = 'example.txt';
writeFile(file, 'Hello, world!');
readFileAndPrint(file);



