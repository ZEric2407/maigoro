<script>
	import { A } from 'flowbite-svelte';
	import { Section, Faq, FaqItem } from 'flowbite-svelte-blocks';
	import { HeartSolid } from 'flowbite-svelte-icons';
</script>

<p class="about-text">
	Are you tired of accidentally eating dog meat while visiting a foreign country? Are you tired of bugs 
    showing up in your cheese? Don't worry, we got you! Maigoro is a handy app designed to make sure that you
    know exactly what you're about to bite into: Just take a picture and we'll provide you with a translation, 
    as well as some cultural context of whatever you're about to bite into! 
</p>

<Section name="faq" sectionClass="py-0 [&>div]:py-8">
	<h2 class="mb-8 text-4xl font-extrabold tracking-tight text-gray-900 dark:text-white">
		Frequently Asked Questions (FAQs)
	</h2>
	<Faq>
		<div>
			<FaqItem>
				<svelte:fragment slot="h3">What does Maigorou mean?</svelte:fragment>
				<p class="text-gray-500 dark:text-gray-400">
					Maigoro ( /ˈmaɪ-goʊ-roʊ/, also MY-go-roh ) is the 
					personal guru that spiritually guides one, connecting 
					one's mind with wisdom. It may offer help to one's inner 
					and outer journey by giving a deeper insight to the world. 
					Being able to help one in a moment of doubt, maigoro will 
					allow one to reach a deeper level of understanding of their environment.
				</p>
			</FaqItem>
			<FaqItem>
				<svelte:fragment slot="h3">Can I upload pictures directly from my app?</svelte:fragment>
				<p class="text-gray-500 dark:text-gray-400">
					yessirrrrr
				</p>
			</FaqItem>
		</div>
	</Faq>
</Section>

<style>
	.about-text {
		@apply text-gray-900 dark:text-gray-100;
	}
</style>