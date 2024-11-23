<script lang="ts">
	import '../app.css';
	import {
		Navbar,
		NavBrand,
		NavLi,
		NavUl,
		NavHamburger,
		DarkMode,
		P
	} from 'flowbite-svelte';
	import {
		Footer,
		FooterLinkGroup,
		FooterLink
	} from 'flowbite-svelte';
	import { goto } from '$app/navigation';

	function reloadPage() {
		goto('/').then(() => {
			window.location.reload();
		});
	}

</script>

<div class="container mx-auto">
	<Navbar
		rounded
		color="form"
		class="sticky start-0 top-0 z-20 w-full px-2 py-2.5 sm:px-4"
		id="top-nav"
	>
		<NavBrand href="/" on:click={reloadPage}>
			<img src="/tibo.jpg" class="ml-2 mr-2 h-16 w-16 rounded-full" alt="Logo" />
			<P class="font-sans text-xl font-semibold text-[#4C8C2B]">Maigoro</P>
		</NavBrand>

		<div class="flex md:order-2">
			<DarkMode />
			<NavHamburger />
		</div>

		<NavUl>
			<NavLi href="/" class="mr-4" on:click={reloadPage}>Home</NavLi>
			<NavLi href="/about" class="mr-4">About</NavLi>
			<NavLi href="/contact-us" class="mr-4">Contact Us</NavLi>
		</NavUl>
	</Navbar>
</div>


<!-- Footer -->
<footer class="mt-auto flex items-center justify-center bg-gray-100 py-4 dark:bg-gray-800">
	<Footer>
		<div class="flex items-center justify-center">
			<p class="text-sm text-gray-500 dark:text-gray-400">© 2024 Maigoro.</p>
			<FooterLinkGroup
				ulClass="flex flex-wrap items-center ml-2 mt-3 text-sm text-gray-500 dark:text-gray-400 sm:mt-0 underline"
			>
				<FooterLink href="https://github.com/ZEric2407/maigoro"
					>See Our Source Code</FooterLink
				>
			</FooterLinkGroup>
		</div>
	</Footer>
</footer>

<style lang="postcss">
	:global(body) {
		@apply flex min-h-screen flex-col bg-white dark:bg-gray-900;
	}

	:global(#app) {
		@apply flex min-h-screen flex-col;
	}

	:global(main) {
		@apply flex flex-grow flex-col;
	}
</style>