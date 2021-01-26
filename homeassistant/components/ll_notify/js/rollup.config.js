import resolve from "@rollup/plugin-node-resolve";
import globals from "rollup-plugin-node-globals";
import builtins from "rollup-plugin-node-builtins";
import babel from "@rollup/plugin-babel";
import serve from "rollup-plugin-serve";
import json from "@rollup/plugin-json";
import commonjs from "@rollup/plugin-commonjs";
import postcss from "rollup-plugin-postcss";
import { terser } from "rollup-plugin-terser";

const dev = process.env.ROLLUP_WATCH;

const servopts = {
  contentBase: "./dist",
  host: "0.0.0.0",
  port: 5000,
  allowCrossOrigin: true,
  headers: {
    "Access-Control-Allow-Origin": "*",
  },
};

export default {
  input: ["src/ll_notify.js"],
  output: {
    dir: "./dist",
    format: "es",
  },
  plugins: [
    resolve({
      preferBuiltins: true,
    }),
    json(),
    postcss({
      plugins: [],
    }),
    babel({
      exclude: "node_modules/**",
      babelHelpers: 'bundled'
    }),
    commonjs({
      esmExternals: true,
      transformMixedEsModules: true,
    }),
    globals(),
    builtins(),
    dev && serve(servopts),
    // !dev && terser()
  ],
};
