"use strict";
/* global __dirname */

module.exports = function () {
  return {
    module: {
      rules: [{
        test: /\.js$/i,
        loader: "babel-loader",
        options: {
          presets: ["@babel/preset-env"],
          plugins: [
            "@babel/plugin-proposal-class-properties"
          ]
        }
      }]
    }
  };
};
