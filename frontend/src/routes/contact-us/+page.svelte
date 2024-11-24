<script>
	import { P } from 'flowbite-svelte';
</script>

<P class="mt-5 text-center text-2xl font-bold text-gray-900 dark:text-gray-100">
	Team Members
</P>


<ul class="flex list-none flex-wrap justify-center p-0">
	<li class="contact-item">
		<a href="https://github.com/j279li" target="_blank" rel="noopener noreferrer">
			<strong>Jack</strong>
	</a>
	</li>
	<li class="contact-item">
		<a href="https://github.com/ZEric2407" target="_blank" rel="noopener noreferrer">
			<strong>Eric</strong>
		</a>
	</li>
	<li class="contact-item">
		<a href="https://github.com/Kaos1" target="_blank" rel="noopener noreferrer">
			<strong>Thibaut</strong>
		</a>
	</li>
	<li class="contact-item">
		<a href="https://github.com/SteamyFuton" target="_blank" rel="noopener noreferrer">
			<strong>Frank</strong>
		</a>
	</li>
</ul>


<style>
	.contact-item {
		margin: 10px 20px;
		padding: 15px;
		border: 2px solid #ffffff;
		border-radius: 8px;
		background-color: #083950;
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
		color: #e9d7ee;
	}
</style>