const path = require("path");

module.exports = {
  outputDir: path.resolve(__dirname, "../static"),
  assetsDir: "",
  publicPath: "/static",
  indexPath: path.resolve(__dirname, "../templates/index.html"),
};
