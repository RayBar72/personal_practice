#!/usr/bin/env node


const arg = process.arg
const largo = process.length

if (largo == 2) {
    console.log('No argument')
} else if (largo == 3) {
    console.log('Argument found')
} else {
    console.log('Arguments found')
}
console.log(${arg})