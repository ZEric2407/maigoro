const { sveltekit } = require("@sveltejs/kit/vite");
const { defineConfig } = require("vitest/config");

module.exports = defineConfig({
  plugins: [sveltekit()],
  test: {
    include: ["src/**/*.{test,spec}.{js,ts}"],
  },
});