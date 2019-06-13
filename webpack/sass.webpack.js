"use strict";

module.exports = function () {
  return {
    module: {
      rules: [{
        test: /\.sass$/i,
        use: [{
          loader: "file-loader?name=../css/[name].css"
        },{
          loader: "extract-loader"
        },{
          loader: "css-loader?url=false"
        },{
          loader: "sass-loader"
        }]
      }]
    }
  };
};
