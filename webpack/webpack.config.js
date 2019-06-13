'use strict';
/* global __dirname */

const p = require("path");
const merge = require("webpack-merge");

const path = require("./path.webpack.js");
const pug = require("./pug.webpack.js");
const sass = require("./sass.webpack.js");
const js = require("./js.webpack.js");
const img = require("./image.webpack.js");
const font = require("./font.webpack.js");

const settings = merge([{
  entry: path.app,
  output: {
    path: p.join(__dirname, "/dist/js/"),
    filename: "[name].js",
    publicPath: "/dist"
  },
  resolve: {
    modules: ["node_modules"]
  },
  devServer: {
    overlay: true,
    open: path.browser,
    contentBase: p.join(__dirname, "/dist"),
    compress: true,
    port: 3000
  },
  watch: true
},
pug(),
sass(),
js(),
img(),
font()]);

module.exports = (env, options) => {
  settings.devtool = options.mode === "production"
    ? false
    : "cheap-module-eval-source-map";

  return settings;
};
