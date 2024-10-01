const path = require("path");

module.exports = {
  outputDir: path.resolve(__dirname, "../static"),
  assetsDir: "",
  publicPath: "/static",
  indexPath: path.resolve(__dirname, "../templates/index.html"),
  chainWebpack: (config) => {
    config.plugin("copy").tap(([options]) => {
      options.patterns.push({
        from: path.resolve(__dirname, "public/images"),
        to: path.resolve(__dirname, "../static/images"),
        toType: "dir",
        noErrorOnMissing: true,
        globOptions: {
          ignore: [".DS_Store"],
        },
      });
      return [options];
    });
  },
};
