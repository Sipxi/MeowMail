/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.html"],
  theme: {
    extend: {
      colors: {
        drip: "#4ade80",
        flame: "#f87171",
      },
      fontFamily: {
        drip: ["'Comic Neue'", "cursive"]
      }
    },
  },
  plugins: [],
};
