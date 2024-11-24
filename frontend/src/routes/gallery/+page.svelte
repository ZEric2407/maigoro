<script>
    import { onMount } from 'svelte';
    import { Popover } from 'flowbite-svelte';
    import { QuestionCircleSolid, ChevronRightOutline } from 'flowbite-svelte-icons';
    import { Button, Modal } from 'flowbite-svelte';
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
                    modalOpen: false,
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

<h1 class="mb-8 text-4xl font-extrabold tracking-tight text-gray-900 dark:text-white" style="margin-top: 1%; margin-left:5%;">History (6 most recent)</h1>
<div class="grid grid-cols-2 md:grid-cols-3 gap-4" style="margin:5%; margin-top:1%">
    {#each images as image}
        <div class="relative group">
            <!-- Image -->
            <div>
            <img 
                src={image.src} 
                alt={image.alt} 
                class="cursor-pointer rounded-lg shadow hover:shadow-lg"
                onclick="{() => (image.modalOpen = true)}"
            />
            <Modal title="Cultural Significance" bind:open={image.modalOpen} autoclose>
                <p class="text-base leading-relaxed text-gray-500 dark:text-gray-400"><b>Cultural Significance: </b>{image.culturalSignificance}</p>
                {#if image.translatedText}
                <p class="text-base leading-relaxed text-gray-500 dark:text-gray-400"><b>Translated Text: </b>{image.translatedText}</p>
                {/if}
                <svelte:fragment slot="footer">
                  <Button color="alternative">Back</Button>
                </svelte:fragment>
              </Modal>
            </div>
        </div>
    {/each}
</div>
