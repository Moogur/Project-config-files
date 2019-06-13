"use strict";

module.exports = function () {
  return {
    module: {
      rules: [{
        test: /\.(jpg|jpeg|png)$/i,
        use: [{
          loader: "file-loader?name=../img/[name].[ext]"
        },{
          loader: "image-webpack-loader",
          options: {
            mozjpeg: {
              progressive: true,
              quality: 75
            },
             pngquant: {
              force: 256,
              speed: 1
            },
          }
        }]
      }]
    }
  }
}
