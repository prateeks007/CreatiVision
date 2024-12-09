const { defineConfig } = require("@vue/cli-service");
const path = require("path");

module.exports = defineConfig({
  devServer: {
    historyApiFallback: true,
  },
  transpileDependencies: true,
  outputDir: path.resolve(__dirname, "../static"),
  assetsDir: "",
  publicPath: "/static",
  indexPath: path.resolve(__dirname, "../templates/index.html"),
});
