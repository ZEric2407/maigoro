<script>
	import { P } from 'flowbite-svelte';
</script>

<P class="mt-5 text-center text-2xl font-bold text-gray-900 dark:text-gray-100">
	Team Members
</P>


<ul class="flex list-none flex-wrap justify-center p-0">
	<li class="contact-item">
		<strong>Eric</strong>
	</li>
	<li class="contact-item">
		<strong>Jack</strong>
	</li>
	<li class="contact-item">
		<strong>Thibaut</strong>
	</li>
	<li class="contact-item">
		<strong>Frank</strong>
	</li>
</ul>


<style>
	.contact-item {
		margin: 10px 20px;
		padding: 15px;
		border: 2px solid #bb2b1e;
		border-radius: 8px;
		background-color: #fdeeec;
		width: 12vw;
		text-align: center;
		transition: transform 0.2s ease-in-out;
	}

	.contact-item:hover {
		transform: scale(1.05);
	}

	.contact-item strong {
		display: block;
		margin-bottom: 5px;
		font-size: 1.2em;
		color: #bb2b1e;
	}
</style>