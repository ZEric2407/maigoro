const js = require("@eslint/js");
const ts = require("@typescript-eslint/eslint-plugin");
const tsParser = require("@typescript-eslint/parser");
const svelte = require("eslint-plugin-svelte");
const prettier = require("eslint-config-prettier");
const globals = require("globals");

module.exports = [
	js.configs.recommended,
	...ts.configs.recommended,
	...svelte.configs["flat/recommended"],
	prettier,
	...svelte.configs["flat/prettier"],
	{
		languageOptions: {
			globals: {
				...globals.browser,
				...globals.node,
			},
		},
	},
	{
		files: ["**/*.svelte"],
		languageOptions: {
			parser: tsParser,
		},
	},
	{
		ignores: ["build/", ".svelte-kit/", "dist/"],
	},
];