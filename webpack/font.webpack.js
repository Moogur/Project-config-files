"use strict";

const copyPlugin = require("copy-webpack-plugin");

module.exports = function () {
  return {
    plugins: [
      new copyPlugin([
        {from: "./app/font", to: "../font"}
      ])
    ],
  }
}