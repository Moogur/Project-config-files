"use strict";

module.exports = function () {
  return {
    module: {
      rules: [{
        test: /\.pug$/i,
        use: [{
          loader: "file-loader?name=../[name].html"
        },{
          loader: "extract-loader"
        },{
          loader: "html-loader"
        },{
          loader: "pug-plain-loader"
        },{
          loader: "pug-bem-plain-loader"
        }]
      }]
    }
  };
};
