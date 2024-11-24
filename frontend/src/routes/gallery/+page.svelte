<script>
    import { onMount } from 'svelte';
    import { Popover } from 'flowbite-svelte';
    import { QuestionCircleSolid, ChevronRightOutline } from 'flowbite-svelte-icons';

    let images = []; // Reactive variable for images

    const getTransactions = async () => {
        try {
            const response = await fetch('http://localhost:5000/api/gallery', {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                },
            });

            if (response.ok) {
                const data = await response.json();
                console.log('Backend response:', data);

                // Update images with reactivity in mind
                images = data.transactions.map((transaction, i) => ({
                    id: `image-${i}`, // Unique ID for Popover trigger
                    alt: `Image ${i}`,
                    src: `http://localhost:5000/${transaction.image_url.replace("\\", "/")}`,
                    translatedText: transaction.translated_text,
                    culturalSignificance: transaction.cultural_significance,
                }));

                console.log('Updated images:', images); // Debugging
                return data;
            } else {
                console.error('Error fetching images from backend:', response.statusText);
            }
        } catch (error) {
            console.error('Error during backend call:', error);
        }
    };

    onMount(async () => {
        await getTransactions();
    });
</script>

<div class="grid grid-cols-2 md:grid-cols-3 gap-4">
    {#each images as image}
        <div class="relative group">
            <!-- Image -->
            <img 
                src={image.src} 
                alt={image.alt} 
                class="cursor-pointer rounded-lg shadow hover:shadow-lg"
            />

            <!-- Info Icon and Popover -->
            <div class="absolute bottom-2 right-2 flex items-center text-sm font-light text-gray-500 dark:text-gray-400">
                <button id={image.id} class="flex items-center">
                    <QuestionCircleSolid class="w-5 h-5 ms-1.5" />
                    <span class="sr-only">Show information</span>
                </button>
                <Popover
                    triggeredBy={`#${image.id}`}
                    class="w-72 text-sm font-light text-gray-500 bg-white dark:bg-gray-800 dark:border-gray-600 dark:text-gray-400"
                    placement="bottom-start"
                >
                    <div class="p-3 space-y-2">
                        <h3 class="font-semibold text-gray-900 dark:text-white">
                            Cultural Significance
                        </h3>
                        <p>{image.culturalSignificance}</p>
                        <h3 class="font-semibold mt-4 text-gray-900 dark:text-white">
                            Translated Text
                        </h3>
                        <p>{image.translatedText}</p>
                    </div>
                </Popover>
            </div>
        </div>
    {/each}
</div>
